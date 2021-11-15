<template>
    <div>
        <el-container>
            <el-header style="text-align: right; line-height: 60px;">
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
                <div class="formSet">
                    <h3>TripNow旅行计划定制</h3>
                    <el-divider></el-divider>
                    <el-form :model="planForm" :rules="rules" status-icon ref="planForm" class="demo-planForm">
                        <el-form-item label="标签" prop="interest">
                            <el-select v-model="planForm.interest" multiple placeholder="请选择">
                                <el-option :label="'城市观光'" value=1></el-option>
                                <el-option :label="'澳门景点'" value=2></el-option>
                                <el-option :label="'历史人文'" value=3></el-option>
                                <el-option :label="'主题公园'" value=4></el-option>
                                <el-option :label="'自然风光'" value=5></el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="预计人数" prop="number">
                            <el-input v-model="planForm.number" placeholder="请输入内容"> </el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm('planForm')">提交</el-button>
                        </el-form-item>
                         <el-form-item>
                           <p>{{msg}}</p>
                        </el-form-item>
                        
                    </el-form>
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "Plan",
        data() {
            var vNumber = (rule, value, callback) => {
                if (!(/^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$/).test(value)) {
                    callback(new Error('请输入数字值'))
                } else if(value < 1 || value > 10) {
                    callback(new Error('人数限制：1-10！'))
                } else {
                    callback()
                }
            }

            return {
                planForm: {
                    interest: [],
                    number: '',
                },
                rules: {
                    interest: [
                        { required: true, message: '请选择心仪标签', trigger: 'change' },
                    ],
                    number: [
                        { required: true, message: '请决定出行人数', trigger: 'change' },
                        { validator: vNumber, trigger: 'blur' },
                    ],

                },
                username: '',
                msg: '',
            };
        },
        methods: {
            toRegister() {
                this.$router.push("register");
            },
            toIndex() {
                this.$router.push("/");
            },
            printValue() {
                console.log(this.planForm.number);
            },
            logout() {
                sessionStorage.removeItem("accessToken")
                this.$message.success("Logout Successful");
                this.reload();
            },
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                      this.$message.success("为您推荐以下景点：）")
                        this.$router.push({
                            name: 'choice', 
                            params: {
                                labels: this.planForm.interest,
                                number: this.planForm.number,
                            }
                        });
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
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

    .headIcon {
        width: 150px;
        height: 60px;
        background-image: url(../assets/ZHimg/icon-black.png);
        background-size: cover;
    }
</style>