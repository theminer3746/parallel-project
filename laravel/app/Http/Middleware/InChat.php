<?php

namespace App\Http\Middleware;

use Closure;
use App\Chat;

class InChat
{
    /**
     * Handle an incoming request.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \Closure  $next
     * @return mixed
     */
    public function handle($request, Closure $next)
    {
        $chat = new Chat;

        if ($chat->isUserInChat($request->route('chat_id'), auth()->payload()->get('sub'))) {
            return $next($request);
        } else {
            return response()->json([
                'message' => 'The user do not belong to this chat'
            ], 403);
        }
    }
}
