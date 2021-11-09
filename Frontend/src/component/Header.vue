
<template>
    <div class="header">
          <nav class="navbar navbar-dark navbar-expand-lg mb-4  bg-dark fixed-top navbar-shrink" id="mainNav">
              <div class="container"><a class="navbar-brand js-scroll-trigger" href="#" style="margin-top:-0.5%;"><img src="../assets/img/logo.jpg" width="18%" alt="Logo"></a><button class="navbar-toggler navbar-toggler-right" data-toggle="collapse" data-target="#navbarResponsive" type="button" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation"><i class="fa fa-align-justify"></i></button>
                  <div class="collapse navbar-collapse" id="navbarResponsive">
                      <ul class="nav navbar-nav ml-auto">

                          <li class="nav-item" role="presentation">
                            <router-link to="/" >
                              <span class="nav-link js-scroll-trigger" style="font-size: 15.2px !important">
                                  ACCEUIL
                                  </span>
                                </router-link>
                            </li> 
                            
                      </ul>
                  </div>
              </div>
          </nav>
      </div>
</template>

    <script>
  export default {
      name:'Header',
      props:{

      },
      computed:{
      },
      data:function() {
        return{
        }
    },
  }
</script>

<style>
/* Header*/
.header{
    margin-bottom: 10vh;
}

</style>