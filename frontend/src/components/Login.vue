<template>
    <div>
        <el-container>
            <el-header style="text-align: right; line-height: 60px;">
                <el-row>
                    <el-col :span="12" style="text-align: left;">
                        <div class="headIcon" @click="$router.push('/')">
                        </div>
                    </el-col>

                </el-row>
            </el-header>
            <el-main>
                <el-row :gutter="20">
                    <el-col :span="12">
                        <div class="iconSet">
                        </div>
                    </el-col>
                    <el-col :span="12">
                        <div class="formSet">
                            <h3>登录TripNow</h3>
                            <el-divider></el-divider>
                            <el-form :model="loginForm" status-icon :rules="rules" ref="loginForm"
                                class="demo-loginForm" id="labelColor">
                                <el-form-item label="手机号" prop="phone">
                                    <el-input type="input" v-model="loginForm.phone" clearable placeholder="请输入手机号"
                                        autocomplete="off" suffix-icon="el-icon-phone-outline"></el-input>
                                </el-form-item>
                                <el-form-item label="密码" prop="password">
                                    <el-input type="password" v-model="loginForm.password" clearable placeholder="请输入密码"
                                        autocomplete="off" suffix-icon="el-icon-lock"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="danger" @click="submitForm('loginForm')">提交</el-button>
                                </el-form-item>
                                <el-form-item>
                                    <el-link type="primary" @click="toRegister()">没有账号？去注册</el-link>
                                </el-form-item>
                            </el-form>
                        </div>
                    </el-col>
                </el-row>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "Login",
        data() {
            return {
                loginForm: {
                    phone: '',
                    password: '',
                },
                rules: {
                    phone: { required: true, message: '请输入手机号', trigger: 'blur' },
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
                        const path = 'http://127.0.0.1:5000/login';
                        axios.post(path, {
                            phone: this.loginForm.phone,
                            password: this.loginForm.password
                        }).then((res) => {
                            console.log(res.data);
                            if (res.data.status == 'ok') {
                                sessionStorage.setItem('accessToken', JSON.stringify(res.data.session))
                                this.$message.success("登录成功");
                                this.$router.push("/");
                            }
                            else {
                                this.$message.error(res.data.info);
                                console.log('error submit!!');
                                return false;
                            }
                        }).catch(function (error) {
                            console.error(error);
                            return false;
                        })
                    }
                    else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
        },
        creater() {
            this.submitForm(formName);
        },
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
        background-image: url(../assets/ZHimg/night.jpg);
        background-size: cover;
        color: black;
        text-align: center;
        line-height: 40px;
    }

    .el-divider {
        background-color: #ffffff;
    }

    #labelColor>>>.el-form-item__label {
        color: #000000;
        font-size: 14px;
    }

    .formSet {
        width: 300px;
        background-color: rgb(255, 255, 255, 0.75);
        border-radius: 5px;
        color: black;
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