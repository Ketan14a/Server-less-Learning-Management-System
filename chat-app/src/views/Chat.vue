
// The following idea is taken from : https://www.youtube.com/watch?v=lcYn0tgUvHE&t=1619s

<template>
    <div class="container chat">
        <h2 class="text-primary text-center">Chat Application Using FireBase </h2>
        <div class="card">
            <div class="card-body">
                <p class="text-secondary nomessages" v-if="messages.length == 0">
                    [No message!]
                </p>
                <div class="messages" v-chat-scroll="{always: false, smooth: true}">
                    <div v-for="message in messages" :key="message.id">
                        <span class="text-info"> [{{ message.name }}] : </span>
                        <span>{{message.message}}</span>
                        
                    </div>
                </div>
            </div>
            <div class="card-action">
                <CreateMessage :name="name"/>
            </div>
        </div>
    </div>
</template>

<script src="chat.js">

</script>

<style>

@import './style.css'

</style>