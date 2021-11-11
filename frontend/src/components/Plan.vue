<template>
    <div>
        <el-container>
            <el-header style="text-align: right; line-height: 60px;">
                <el-row>
                    <el-col :span="12" style="text-align: left;">
                        <el-button type="plain" @click="toIndex">首页</el-button>
                        </el-button>
                    </el-col>
                    <el-col :span="12" style="text-align: right;">
                        <el-button type="plain">用户名</el-button>
                        <el-button type="plain">退出登录</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <div class="formSet">
                    <h3>TripNow旅行计划定制</h3>
                    <el-divider></el-divider>
                    <el-form :model="planForm" status-icon ref="planForm" class="demo-planForm">
                        <el-form-item label="标签" prop="liked">
                            <el-select v-model="planForm.value1" multiple placeholder="请选择">
                                <el-option label="区域一" value="shanghai"></el-option>
                                <el-option label="区域二" value="beijing"></el-option>
                                <el-option label="区域三" value="guangzhou"></el-option>
                                <el-option label="区域四" value="changsha"></el-option>
                                <el-option label="区域五" value="zhongshan"></el-option>
                                <el-option label="区域六" value="zhuhai"></el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="密码" prop="password">
                            <el-input type="password" v-model="planForm.password" clearable placeholder="请输入密码"
                                autocomplete="off"></el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm('planForm')">提交</el-button>
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
        name: "Plan",
        data() {
            return {
                planForm: {
                    password: '',
                    value1: [],
                },
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
        width: 600px;
        background-color: #ffffff;
        border-radius: 5px;
        margin: auto;
        padding: 20px;
    }
</style>