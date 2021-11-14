<template>
    <div>
        <el-container>
            <el-header style=" line-height: 60px;">
                <el-row>
                    <el-col :span="12" style="text-align: left;">
                        <div class="headIcon" @click="$router.push('/')">
                        </div>
                    </el-col>
                    <el-col v-if="username == ''" span="12" style="text-align: right;">
                        <el-button type="danger" @click="toLogin"> 登录 </el-button>
                        <el-button type="danger" @click="toRegister">注册</el-button>
                    </el-col>
                    <el-col v-else span="12" style="text-align: right;">
                        <el-a style="color:grey; font-size:20px; margin-right: 20px;"> 
                            <i class="el-icon-user-solid"></i>
                            <b> {{username}} </b>
                        </el-a>
                        <el-button type="text" icon="el-icon-switch-button" @click="logout" plain>退出登录</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <el-row :gutter="20">
                    <el-col :span="12">
                        <div class="grid-content bg-purple">
                            <el-carousel height="400px">
                                <el-carousel-item v-for="item in imgs" :key="item.name">
                                    <el-image :src="item.img"></el-image>
                                </el-carousel-item>
                            </el-carousel>
                        </div>
                    </el-col>
                    <el-col :span="12">
                        <div class="grid-content bg-purple-light">
                            <el-carousel height="400px">
                                <el-carousel-item v-for="item in imgs" :key="item.name">
                                    <el-image :src="item.img"></el-image>
                                </el-carousel-item>
                            </el-carousel>
                        </div>
                    </el-col>
                </el-row>
                <div style="padding: 50px;">
                    <el-button type="danger" @click="toPlan">开始制定计划！</el-button>
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import img1 from "../assets/ZHimg/spring.jpg";
    import img2 from "../assets/ZHimg/summer.jpg";
    import img3 from "../assets/ZHimg/fall.jpg";
    import img4 from "../assets/ZHimg/winter.jpg";

    export default {
        inject:['reload'],
        name: "Container",
        data() {
            return {
                imgs: [
                    { img: img1, name: 'spring' },
                    { img: img2, name: 'summer' },
                    { img: img3, name: 'fall' },
                    { img: img4, name: 'winter' },
                ],
                username: '',
            };
        },
        methods: {
            toLogin() {
                this.$router.push("/login");
            },
            toRegister() {
                this.$router.push("/register");
            },
            toPlan() {
                this.$router.push("/plan");
            },
            logout(){
                sessionStorage.removeItem("accessToken")
                this.$message.success("Logout Successful");
                this.reload();
            }

        },
        created(){
            let curr_user = sessionStorage.getItem('accessToken')
            if (curr_user){
                this.username = JSON.parse(curr_user)
            }
        }

    };
</script>

<style scoped>
    .el-header {
        background-color: #ffffff;
        color: #333;
        border-radius: 1px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }

    .el-main {
        background-color: #E9EEF3;
        color: #333;
        text-align: center;
    }

    .el-carousel__item h3 {
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        line-height: 200px;
        margin: 0;
    }

    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }

    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }

    .headIcon {
        width: 150px;
        height: 60px;
        background-image: url(../assets/ZHimg/icon-black.png);
        background-size: cover;
    }
</style>