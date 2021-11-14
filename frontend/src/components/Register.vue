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
                        <el-button type="danger" plain @click="toLogin">登录</el-button>
                        <el-button type="danger" @click="toRegister">注册</el-button>
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
                            <h3>注册TripNow账号</h3>
                            <el-divider></el-divider>
                            <el-form :model="regisForm" status-icon :rules="rules" ref="regisForm"
                                class="demo-regisForm">
                                <el-form-item label="用户名" prop="username">
                                    <el-input type="input" v-model="regisForm.username" clearable placeholder="请输入用户名"
                                        autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item label="密码" prop="password">
                                    <el-input type="password" v-model="regisForm.password" clearable placeholder="请输入密码"
                                        autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item label="确认密码" prop="passCheck">
                                    <el-input type="password" v-model="regisForm.passCheck" clearable
                                        placeholder="请确认密码" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item label="电话号" prop="phonenumber">
                                    <el-input type="input" v-model="regisForm.phonenumber" clearable
                                        placeholder="请输入电话号码" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item label="邮箱地址" prop="mailAddress">
                                    <el-input type="input" v-model="regisForm.mailAddress" clearable
                                        placeholder="请输入邮箱地址" autocomplete="off"></el-input>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="danger" @click="submitForm('regisForm')">提交</el-button>
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
    export default {
        name: "Register",
        data() {
            var vPassword = (rule, value, callback) => {
                if (value !== this.regisForm.password) {
                    callback(new Error('两次输入密码不一致！'));
                } else {
                    callback();
                }
            }

            var vPhone = (rule, value, callback) => {
                if (value && (!(/^[1][345789]\d{9}$/).test(value) || !(/^[1-9]\d*$/).test(value))) {
                    callback(new Error('手机号码不符合规范'))
                } else {
                    callback()
                }

            }

            var vMail = (rule, value, callback) => {
                let temp = /^[\w.\-]+@(?:[a-z0-9]+(?:-[a-z0-9]+)*\.)+[a-z]{2,3}$/
                let tempOne = /^[A-Za-zd]+([-_.][A-Za-zd]+)*@([A-Za-zd]+[-.])+[A-Za-zd]{2,5}$/
                if (value && (!(temp).test(value))) {
                    callback(new Error('邮箱格式不符合规范'))
                } else {
                    callback()
                }
            }

            return {
                regisForm: {
                    username: '',
                    phonenumber: '',
                    mailAddress: '',
                    password: '',
                    passCheck: '',
                },
                rules: {
                    username: [
                        { required: true, message: '请输入用户名', trigger: 'blur' },
                        { min: 5, max: 20, message: '长度在5到20个字符之间', trigger: 'blur' },
                    ],
                    phonenumber: [
                        { required: true, message: '请输入联系方式', trigger: 'blur' },
                        { min: 11, max: 11, message: '长度应为11位', trigger: 'blur' },
                        { validator: vPhone, trigger: 'blur' },
                    ],
                    mailAddress: [
                        { required: true, message: '请输入邮箱地址', trigger: 'blur' },
                        { min: 5, max: 20, message: '长度在5到20个字符之间', trigger: 'blur' },
                        { validator: vMail, trigger: 'blur' },
                    ],
                    password: [
                        { required: true, message: '请输入密码', trigger: 'blur' },
                        { min: 5, max: 20, message: '长度在5到20个字符之间', trigger: 'blur' },
                    ],
                    passCheck: [
                        { required: true, message: '请确认密码', trigger: 'blur' },
                        { validator: vPassword, trigger: 'blur' },
                    ],
                }
            }
        },
        methods: {
            toLogin() {
                this.$router.push("login");
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
    .el-header {
        background-color: #ffffff;
        color: #333;
        border-radius: 1px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }

    .el-main {
        background-image: url(../assets/ZHimg/day.jpg);
        background-size: cover;
        color: #333;
        text-align: center;
        line-height: 40px;
    }

    .formSet {
        width: 300px;
        background-color: #ffffff;
        border-radius: 5px;
        margin: auto;
        padding: 20px;
        margin-top: 50px;
        margin-bottom: 50px;
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
        background-image: url(../assets/ZHimg/icon-black-all.png);
        background-size: cover;
    }
</style>