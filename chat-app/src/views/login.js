export default {
    name: 'userlogin',
    data () {
        return {
            name: "",
            errorText: null
        }
    },
    methods: {
        userlogin() {
            //let users = [{name:"Varun",email:"varunchauhan136@gmail.com"},{name:"Gunnet",email:"xyz@gmail.com"}]
            let c= ["varunchauhan136@gmail.com","ketan.bhalerao@dal.ca","sr950863@dal.ca","gunnet@dal.ca"]
            if (c.includes(this.name)) {
                if(this.name==="varunchauhan136@gmail.com")
                this.$router.push({name: 'Chat', params: {name: "Varun"}});
            } else if (this.name==="ketan.bhalerao@dal.ca"){
                this.$router.push({name: 'Chat', params: {name: "ketan"}});
            }
            else if (this.name==="sr950863@dal.ca"){
                this.$router.push({name: 'Chat', params: {name: "Sri"}});
            }
            else if (this.name==="gunnet@dal.ca"){
                this.$router.push({name: 'Chat', params: {name: "Guneet"}});
            }else {
                this.errorText = "You are not allowed to enter in this room"
            }
        }
    }
}