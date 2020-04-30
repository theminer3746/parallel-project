<?php

namespace App;

class MessageDto
{
    /**
     * Message
     * 
     * @var string
     */
    public $message;

    /**
     * user_id of the message author
     * 
     * @var string
     */
    public $userId;

    public function __construct($message, $userId)
    {
        $this->message = $message;
        $this->userId = $userId;
    }
}
