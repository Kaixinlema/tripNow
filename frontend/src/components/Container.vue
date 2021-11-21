<template>
    <div>
        <el-container>
            <el-header  style="line-height: 60px;  -webkit-box-shadow: none;
box-shadow: none; background-color: rgba(153, 204, 255, 0.15);">
                <el-row>
                    <el-col :span="12" style="text-align: left;">
                        <div class="headIcon" @click="$router.push('/')">
                        </div>
                    </el-col>
                    <el-col v-if="username == ''" :span="12" style="text-align: right;">
                        <el-button type="danger" @click="toLogin"> 登录 </el-button>
                        <el-button type="danger" @click="toRegister">注册</el-button>
                    </el-col>
                    <el-col v-else :span="12" style="text-align: right;">
                        <el-a style="color:grey; font-size:20px; margin-right: 20px;">
                            <i class="el-icon-user-solid"></i>
                            <b> {{username}} </b>
                        </el-a>
                        <el-button type="text" icon="el-icon-switch-button" @click="logout" plain>退出登录</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main style=" background-color: rgba(153, 204, 255, 0.15);">
                <div class="mainPage">
                    <div class="mainContent">
                        <el-button type="text" @click="toPlan" style="font-size: 25px; color:#ffffff;">
                            <i class="el-icon-caret-right"></i> 开始制定计划！
                        </el-button>
                    </div>
                </div>


            </el-main>
        </el-container>
    </div>
</template>

<script>

    export default {
        inject: ['reload'],
        name: "Container",
        data() {
            return {
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
            logout() {
                sessionStorage.removeItem("accessToken")
                this.$message.success("Logout Successful");
                this.reload();
            }

        },
        created() {
            let curr_user = sessionStorage.getItem('accessToken')
            if (curr_user) {
                this.username = JSON.parse(curr_user)
            }
        }

    };
</script>

<style scoped>
    .el-header {
        background-color: white;
        color: #333;
        border-radius: 1px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }

    .el-main {
        background-color: white;
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

    .mainPage {
        width: 1040px;
        height: 480px;
        background-image: url(../assets/ZHimg/shell.jpg);
        background-size: cover;
        opacity: 0.8;
        border-radius: 10px;
        padding-top: 100px;
        margin: 20px auto 20px auto;
    }

    .mainContent {
        width: 300px;
        height: 80px;
        font-size: 50px;
        border: 5px solid lightblue;
        border-radius: 50px;
        padding: auto;
        margin: auto;
    }
</style>