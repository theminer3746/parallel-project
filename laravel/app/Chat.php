<?php

namespace App;

use Jenssegers\Mongodb\Eloquent\Model;
use App\User;

class Chat extends Model
{
    public function users()
    {
        return $this->hasMany(User::class);
    }
}
