
<template>
    <div class="main">
        <Header/>
        <div class="container-xl">
            <div class="row">
                <div class="col-md-8 mx-auto">
                    <div class="contact-form">
                        <h1>Modifier une tâche</h1>
                        <p class="hint-text">Vous pouvez le mettre à  jour à tout moment</p>
                        <form @submit.prevent="register()">
                            <div class="row">
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <label for="name">Nom</label>
                                        <input type="text" class="form-control" v-model="info.nom"  id="name" required>
                                    </div>
                                </div>
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <label for="responsable">Responsable</label>
                                        <input type="text" class="form-control" v-model="info.responsable" id="responsable" required>
                                    </div>
                                </div>
                            </div>            
                            <div class="row">
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <label for="statut">Statut</label>
                                        <select name="status" class="form-control" v-model="info.statut" id="statut">
                                            <option value="En cours">En cours</option>
                                            <option value="Bloque">Bloqué</option>
                                            <option value="Fini">Fini</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-sm-6">
                                    <div class="form-group">
                                        <label for="date">Date</label>
                                        <input type="date" class="form-control" v-model="info.date" id="date" required>
                                    </div>
                                </div>
                            </div> 
                            <div class="form-group">
                                <label for="description">Description</label>
                                <textarea class="form-control" id="description" v-model="info.description" rows="5" required></textarea>
                            </div>
                            <input type="submit" class="btn btn-primary" value="Modifier">
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <Footer/>
      </div>
</template>
<script>
    import Header from '@/component/Header.vue'
    import Footer from '@/component/Footer.vue'
    import baseUrl from '../API/baseUrl'
    const axios = require('axios')
    export default {
        name:'Ajouter',
        components:{
            Header,
            Footer,
        },
        props:{

        },
        computed:{
        },
        created(){
            var id = this.$route.params.id
            var params = {
                id:id
            }
            axios.post(this.baseUrl + '/api/read',params)
            .then((res)=>{
                if(res.data){
                    this.info.id =  res.data.id
                    this.info.nom =  res.data.nom
                    this.info.responsable =  res.data.responsable
                    this.info.statut =  res.data.statut
                    this.info.description =  res.data.description
                    this.info.date = new Date().now()
                }
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        data:function() {
            return{
                baseUrl:baseUrl,
                info:{
                    id:0,
                    nom:'',
                    responsable:'',
                    date:null,
                    statut:'',
                    description:''
                }
            }
        },
        methods:{
            register(){
                axios.post(this.baseUrl + '/api/update',this.info)
                .then(()=>{
                    this.$router.push('/')
                })
                .catch((error)=>{
                    console.log(error)
                })
            }
        }
    }
</script>

<style>
    /* Ajouter*/

    body {
        color: #566787;
        background: #f5f5f5;
        font-family: "Open Sans", sans-serif;
    }
    .contact-form {
        padding: 50px;
        margin: 30px 0;
    }
    .contact-form h1 {
        text-transform: uppercase;
        margin: 0 0 15px;
    }
    .contact-form .form-control, .contact-form .btn  {
        min-height: 38px;
        border-radius: 2px;
    }
    .contact-form .btn-primary {
        min-width: 150px;
        background: #299be4;
        border: none;
    }
    .contact-form .btn-primary:hover {
        background: #1c8cd7; 
    }
    .contact-form label {
        opacity: 0.9;
    }
    .contact-form textarea {
        resize: vertical;
    }
    .hint-text {
        font-size: 15px;
        padding-bottom: 15px;
        opacity: 0.8;
    }
    .bs-example {
        margin: 20px;
    }
</style>