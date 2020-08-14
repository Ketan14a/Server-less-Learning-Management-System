// The following idea is taken from : https://www.youtube.com/watch?v=lcYn0tgUvHE&t=1619s

import CreateMessage from '@/components/CreateMessage';
import fb from '@/firebase/init';
import db from '../firebase/init'


export default {
    name: 'Chat',
    props: ['name'],
    components: {
        CreateMessage
    },
    data() {
        return {
            messages: []
        }
    },
    create() {
        let ref = fb.collection('messages')
        let reference = ref ;
        reference.onSnapshot(res => {
            res.docChanges().forEach(result => {
                if (result.type == 'added') {
                    let document = result.doc;
                    this.messages.push({
                        id: document.id,
                        name: document.data().name,
                        message: document.data().message,
                    });
                }
            });
            db.collection('messages').get().then((snapshot)=>{
            snapshot.docs.forEach(element => {
            var output= element.data().message;
            console.log(output)
                });
             });
        });
    },
  
    
}