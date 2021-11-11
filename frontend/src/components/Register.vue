<template>
    <div>
        <el-container>
            <el-header style="text-align: right; line-height: 60px;">
                <el-row>
                    <el-col :span="12" style="text-align: left;">
                        <el-button type="plain">图标</el-button>
                        <el-button type="plain" @click="toIndex">首页</el-button>
                    </el-col>
                    <el-col :span="12" style="text-align: right;">
                        <el-button type="plain" @click="toLogin">登录</el-button>
                        <el-button type="primary">注册</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <div class="formSet">
                    <h3>注册TripNow账号</h3>
                    <el-divider></el-divider>
                    <el-form :model="regisForm" status-icon ref="regisForm" class="demo-regisForm">
                        <el-form-item label="用户名" prop="username">
                            <el-input type="input" v-model="regisForm.username" clearable placeholder="请输入用户名"
                                autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="电话号" prop="phonenumber">
                            <el-input type="input" v-model="regisForm.phonenumber" clearable placeholder="请输入电话号码"
                                autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input type="password" v-model="regisForm.password" clearable placeholder="请输入密码"
                                autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item label="确认密码" prop="passCheck">
                            <el-input type="password" v-model="regisForm.passCheck" clearable placeholder="请确认密码"
                                autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm('regisForm')">提交</el-button>
                        </el-form-item>
                    </el-form>
                </div>
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
        name: "Register",
        data() {
            return {
                regisForm: {
                    username: '',
                    phonenumber: '',
                    password: '',
                    passCheck: '',
                },
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

<style>
    .el-header,
    .el-footer {
        background-color: #ffffff;
        color: #333;
        border-radius: 1px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }

    .el-main {
        background-color: #E9EEF3;
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
    }
</style>