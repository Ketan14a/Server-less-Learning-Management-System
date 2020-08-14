//The reference is taken from : https://medium.com/codingthesmartway-com-blog/building-a-real-time-chat-application-with-vue-js-and-firebase-part-1-670c768ad860
import data from '@/firebase/init';

export default {
    name: 'Message',
    props: ['name'],
    data() {
        return {
            newMessage: null,
            errorText: null
        }
    },
    methods: {
        Message () {
            if (this.newMessage) {
                data.collection('messages').add({
                    message: this.newMessage,
                    name: this.name,
                }
            } else {
                this.errorText = "Enter a message";
            }
        }
    }    
}