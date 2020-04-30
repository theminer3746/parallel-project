<?php

namespace App;

use Jenssegers\Mongodb\Eloquent\Model;
use App\Chat;
use App\User;
use App\MessageDto;

class Message extends Model
{
    private $chat;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'message',
    ];

    public function __construct()
    {
        $this->chat = new Chat;
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
}
