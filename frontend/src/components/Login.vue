<template>
    <div>
        <el-container>
            <el-header style="text-align: right; line-height: 60px;">
                <el-row>
                    <el-col :span="12" style="text-align: left;">
                        <div class="headIcon" @click="$router.push('/')">
                        </div>
                    </el-col>
                    <el-col :span="12" style="text-align: right;">
                        <el-button type="danger">登录</el-button>
                        <el-button type="danger" plain @click="toRegister">注册</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <el-row gutter="20">
                    <el-col :span="12">

                        <div class="iconSet">
                        </div>
                    </el-col>
                    <el-col :span="12">
                        <div class="formSet">
                            <h3>登录TripNow</h3>
                            <el-divider></el-divider>
                            <el-form :model="loginForm" status-icon :rules="rules" ref="loginForm"
                                class="demo-loginForm">
                                <el-form-item label="用户名" prop="username">
                                    <el-input type="input" v-model="loginForm.username" clearable placeholder="请输入用户名"
                                        autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item label="密码" prop="password">
                                    <el-input type="password" v-model="loginForm.password" clearable placeholder="请输入密码"
                                        autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="danger" @click="submitForm('loginForm')">提交</el-button>
                                </el-form-item>
                            </el-form>
                        </div>
                    </el-col>
                </el-row>
            </el-main>
            <el-footer style="text-align: center; height: 400ox;">
                <el-row :gutter="20">
                    <el-col :span="6">
                        <h3>联系我们</h3>
                        <p>zy</p>
                        <p>ldy</p>
                    </el-col>
                    <el-col :span="6">
                        <h3>关于我们</h3>
                    </el-col>
                    <el-col :span="6" :offset="6">
                        <h3>合作</h3>
                        <i class="el-icon-share"></i>
                        <i class="el-icon-delete"></i>
                    </el-col>
                </el-row>
            </el-footer>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                loginForm: {
                    username: '',
                    password: '',
                },
                rules: {
                    username: { required: true, message: '请输入用户名', trigger: 'blur' },
                    password: { required: true, message: '请输入密码', trigger: 'blur' },
                }
            }
        },
        methods: {
            toRegister() {
                this.$router.push("register");
            },
            toIndex() {
                this.$router.push("/");
            },
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        alert('submit!');
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
        }
    };
</script>

<style scoped>
    .el-header,
    .el-footer {
        background-color: #ffffff;
        color: #333;
        border-radius: 1px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }

    .el-main {
        background-image: url(../assets/ZHimg/night.jpg);
        background-size: cover;

        color: #333;
        text-align: center;
        line-height: 40px;
    }

    .formSet {
        width: 300px;
        background-color: #ffffff;
        border-radius: 5px;
        margin-top: 50px;
        margin-bottom: 50px;
        margin-left: 20%;
        padding: 20px;
    }

    .headIcon {
        width: 150px;
        height: 60px;
        background-image: url(../assets/ZHimg/icon-black.png);
        background-size: cover;
    }

    .iconSet {
        width: 560px;
        height: 170px;
        margin-top: 30%;
        background-image: url(../assets/ZHimg/icon-white.png);
        background-size: cover;
    }
</style>