css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''


bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn.discordapp.com/attachments/1131837347361722431/1135484223608852580/omega_sojourn_a_robot_user_icon_for_a_website_bbad3e5c-cf1e-49b8-a8a1-d585fec9bef5.png"">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn.discordapp.com/attachments/1131837347361722431/1135480989301350411/omega_sojourn_a_user_icon_for_a_website_e10f3cb9-f851-4f9b-b809-f6b28b0e972d.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''