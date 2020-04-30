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
        $this->find($chatId)->push('user_ids', $userId);
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
}
