
<template>
    <div class="main"> <!--   -->
    <Header/>
    <div class="container-xl">
        <div class="table-responsive">
            <div class="table-wrapper">
                <div class="table-title">
                    <div class="row">
                        <div class="col-sm-5">
                            <h2>Gestion de<b> Tâches</b></h2>
                        </div>
                        <div class="col-sm-7">
                            <router-link to="/ajouter" class="btn btn-secondary"><i class="material-icons">&#xE147;</i> <span>Nouvelle tâche</span></router-link>					
                        </div>
                    </div>
                </div>
                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nom</th>						
                            <th>Date </th>
                            <th>Résponsable</th>
                            <th>Statut</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in items" :key="item.id">
                            <td>{{item.id}}</td>
                            <td><a href="#"> {{item.nom}}</a></td>
                            <td>{{item.date}}</td>                        
                            <td>{{item.responsable}}</td>
                            <td><span class="status text-success">&bull;</span> {{item.statut}}</td>
                            <td>
                                <router-link :to="{name:'Modifier',params:{id:item.id}}"  class="settings" title="Modifier" data-toggle="tooltip"><i class="material-icons">&#xE8B8;</i></router-link>
                                <a href="#" class="delete" title="Effacer" data-toggle="modal"  data-target="#exampleModal"><i @click="showModal(item.id)" class="material-icons">&#xE5C9;</i></a>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">infomation</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <p>Voulez-vous le supprimer?</p>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" @click="undelete()" data-dismiss="modal">Non</button>
                            <button type="button" class="btn btn-primary" @click="deletes()">Oui</button>
                        </div>
                        </div>
                    </div>
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
    import $ from 'jquery'
    const axios = require('axios')
    export default {
        name:'Acceuil',
        components:{
            Header,
            Footer,
        },
        props:{

        },
        data:function() {
            return{
                baseUrl:baseUrl,
                items :[],
                $:$,
                mdpId:null
            }
        },
        computed:{
        },
        created(){
            axios.get(this.baseUrl + '/api/liste')
            .then((res)=>{
                console.log(res.data.task)
                if(res.data.task.length>0){
                    this.items = res.data.task
                }
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        methods:{
            undelete(){
                var self = this
                $('#exampleModal').on('hidden.bs.modal', function (event) {
                    self.mdpId = null
                })
            },
            deletes(){
                if(this.mdpId != null){
                    var self =  this
                    var params={
                        id:self.mdpId
                    }
                    axios.post(this.baseUrl + '/api/delete',params)
                    .then(()=>{
                        this.items = this.items.filter((item)=> item.id != this.mdpId)
                        $('#exampleModal').modal('hide')
                    })
                   
                }
            },
            showModal(id){
                var self = this
                $('#exampleModal').on('show.bs.modal', function (event) {
                    self.mdpId = id
                })
            },
        }
        
    }
</script>

<style>
body {
    color: #566787;
    background: #f5f5f5;
    font-family: 'Varela Round', sans-serif;
    font-size: 13px;
}
.table-responsive {
    margin: 30px 0;
}
.table-wrapper {
    min-width: 1000px;
    background: #fff;
    padding: 20px 25px;
    border-radius: 3px;
    box-shadow: 0 1px 1px rgba(0,0,0,.05);
}
.table-title {
    padding-bottom: 15px;
    background: #299be4;
    color: #fff;
    padding: 16px 30px;
    margin: -20px -25px 10px;
    border-radius: 3px 3px 0 0;
}
.table-title h2 {
    margin: 5px 0 0;
    font-size: 24px;
}
.table-title .btn {
    color: #566787;
    float: right;
    font-size: 13px;
    background: #fff;
    border: none;
    min-width: 50px;
    border-radius: 2px;
    border: none;
    outline: none !important;
    margin-left: 10px;
}
.table-title .btn:hover, .table-title .btn:focus {
    color: #566787;
    background: #f2f2f2;
}
.table-title .btn i {
    float: left;
    font-size: 21px;
    margin-right: 5px;
}
.table-title .btn span {
    float: left;
    margin-top: 2px;
}
table.table tr th, table.table tr td {
    border-color: #e9e9e9;
    padding: 12px 15px;
    vertical-align: middle;
}
table.table tr th:first-child {
    width: 60px;
}
table.table tr th:last-child {
    width: 100px;
}
table.table-striped tbody tr:nth-of-type(odd) {
    background-color: #fcfcfc;
}
table.table-striped.table-hover tbody tr:hover {
    background: #f5f5f5;
}
table.table th i {
    font-size: 13px;
    margin: 0 5px;
    cursor: pointer;
}	
table.table td:last-child i {
    opacity: 0.9;
    font-size: 22px;
    margin: 0 5px;
}
table.table td a {
    font-weight: bold;
    color: #566787;
    display: inline-block;
    text-decoration: none;
}
table.table td a:hover {
    color: #2196F3;
}
table.table td a.settings {
    color: #2196F3;
}
table.table td a.delete {
    color: #F44336;
}
table.table td i {
    font-size: 19px;
}
table.table .avatar {
    border-radius: 50%;
    vertical-align: middle;
    margin-right: 10px;
}
.status {
    font-size: 30px;
    margin: 2px 2px 0 0;
    display: inline-block;
    vertical-align: middle;
    line-height: 10px;
}
.text-success {
    color: #10c469;
}
.text-info {
    color: #62c9e8;
}
.text-warning {
    color: #FFC107;
}
.text-danger {
    color: #ff5b5b;
}
</style>
