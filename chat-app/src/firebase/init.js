import firebase from 'firebase/app';
import 'firebase/firestore';


var configuration = {
  apiKey: "AIzaSyDw6ykBs0k1xmfNJznobepSQKCQajWYu-g",
  authDomain: "chat-application-284622.firebaseapp.com",
  databaseURL: "https://chat-application-284622.firebaseio.com",
  projectId: "chat-application-284622",
  storageBucket: "chat-application-284622.appspot.com",
  messagingSenderId: "1038968305864"
  };
  export let arr = []
  const firebaseApp = firebase.initializeApp(configuration); 
  var db= firebaseApp.firestore() 
   db.collection('messages').get().then((snapshot)=>{
    snapshot.docs.forEach(element => {
        var output= element.data().message;
        arr.push(output)
    });
  });

export default db;