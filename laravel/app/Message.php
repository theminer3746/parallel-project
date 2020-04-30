<?php

namespace App;

use Jenssegers\Mongodb\Eloquent\Model;
use App\Chat;
use App\User;
use App\MessageDto;

class Message extends Model
{
    private $chat;
    private $user;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'message',
    ];

    /**
     * The accessors to append to the model's array form.
     *
     * @var array
     */
    protected $appends = ['username'];

    public function __construct()
    {
        $this->chat = new Chat;
        $this->user = new User;
    }

    public function chat()
    {
        return $this->belongsTo(Chat::class);
    }

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function newMessage($chatId, MessageDto $messageDto)
    {
        $this->chat_id = $chatId;
        $this->user_id = $messageDto->userId;
        $this->message = $messageDto->message;
        $this->save();
    }

    public function getUsernameAttribute()
    {
        return $this->user->find($this->user_id)->username;
    }
}
