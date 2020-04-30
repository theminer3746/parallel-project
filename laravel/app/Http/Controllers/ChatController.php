<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Chat;
use App\User;
use App\Message;
use Exception;

class ChatController extends Controller
{
    private $chat;

    /**
     * Create a new ChatController instance.
     *
     * @return void
     */
    public function __construct(Chat $chat)
    {
        $this->middleware('auth:api');
    
        $this->chat = $chat;
    }

    public function create(Request $request)
    {
        try{
            $chatId = $this->chat->createNewChat($request->name);
            $this->chat->addUserToChat($chatId, auth()->payload()->get('sub'));
            User::find(auth()->payload()->get('sub'))->addUserToChat($chatId, auth()->payload()->get('sub'));
        }catch(Exception $e){
            return response()->json([
                'message' => 'Internal Server Error',
            ], 500);
        }

        return response()->json([], 201);
    }

    public function join(Request $request)
    {
        $this->chat->addUserToChatByInviteCode($request->invite_code, auth()->payload()->get('sub'));

        return response()->json();
    }

    public function newMessage(Request $request, $chatId, Message $message)
    {
        $request->validate([
            'message' => 'required',
            'user_id' => 'required',
        ]);

        $messageDto = new \App\MessageDto($request->message, $request->user_id);

        $message->newMessage($chatId, $messageDto);

        return response()->json([], 201);
    }

    public function getMessage(Request $request, $chatId)
    {
        return $this->chat->getMessagesSinceTime($chatId, $request->since);
    }
}
