<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\User;
use Illuminate\Support\Facades\Hash;

class UserController extends Controller
{
    private $user;

    public function __construct(User $user)
    {
        $this->user = $user;
    }

    public function create(Request $request)
    {
        $request->validate([
            'username' => 'required',
            'password' => 'required',
        ]);

        if ($this->user->where('username', $request->username)->exists()) {
            return response()->json([], 409);
        } else {
            $this->user->insert([
                'username' => $request->username,
                'password' => Hash::make($request->password),
            ]);

            return response()->json([], 201);
        }
    }
}
