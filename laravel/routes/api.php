<?php


/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::group(['middleware' => ['api']], function () {
    Route::group(['prefix' => 'auth'], function () {
        Route::post('login', 'AuthController@login');
        Route::post('logout', 'AuthController@logout');
        Route::post('refresh', 'AuthController@refresh');
        Route::post('me', 'AuthController@me');
    });

    Route::group(['prefix' => 'chats'], function () {
        Route::post('/', 'ChatController@create');
        Route::post('/join', 'ChatController@join');
        Route::post('/{chat_id}/messages', 'ChatController@newMessage')->middleware('in_chat');
        Route::get('/{chat_id}/messages', 'ChatController@getMessage')->middleware('in_chat');
        Route::get('/{chat_id}/invite_code', 'ChatController@getInviteCode')->middleware('in_chat');
    });
});
