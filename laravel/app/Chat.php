<?php

namespace App;

use Jenssegers\Mongodb\Eloquent\Model;
use App\User;
use App\Message;

class Chat extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'invite_code',
    ];

    public function users()
    {
        return $this->hasMany(User::class);
    }

    public function messages()
    {
        return $this->hasMany(Message::class);
    }

    public function createNewChat($name)
    {
        do {
            $inviteCode = sprintf('%06d', random_int(0, 999999));
        } while ($this->where('invite_code', $inviteCode)->exists());

        $chatId = $this->insertGetId([
            'name' => $name,
            'invite_code' => $inviteCode,
        ]);

        return $chatId;
    }

    public function findByInviteCode(string $inviteCode)
    {
        return $this->find($this->getChatIdByInviteCode($inviteCode));
    }

    public function getChatIdByInviteCode(string $inviteCode)
    {
        return $this->where('invite_code', $inviteCode)->value('_id');
    }

    public function addUserToChat($chatId, $userId)
    {
        if (!$this->isUserInChat($chatId, $userId)) {
            $this->find($chatId)->push('user_ids', $userId);
        }
    }

    public function addUserToChatByInviteCode($inviteCode, $userId)
    {
        $this->addUserToChat($this->getChatIdByInviteCode($inviteCode), $userId);
    }

    public function isUserInChat($chatId, $userId)
    {
        return $this->where('_id', $chatId)
            ->where('user_ids', 'all', [$userId])
            ->exists();
    }

    public function isChatExistsByInviteCode($inviteCode)
    {
        return $this->where('invite_code', $inviteCode)->exists();
    }

    public function getMessagesSinceTime(string $chatId, string $since = null)
    {
        $messages = $this->find($chatId)->messages();
        
        if(!is_null($since)){
            $messages = $messages->where('created_at', '>', new \MongoDB\BSON\UTCDateTime($since));
        }

        return $messages->orderBy('created_at', 'asc')
            ->get(['_id', 'message', 'user_id', 'created_at']);
    }

    public function getInviteCodeByChatId($chatId)
    {
        return $this->where('_id', $chatId)->value('invite_code');
    }

    public function getAllChats($userId)
    {
        return $this->where('user_ids', 'all', [$userId])->get();
    }
}
