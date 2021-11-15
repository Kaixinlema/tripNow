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
                        <el-button type="danger" plain>用户名</el-button>
                        <el-button type="danger" plain>退出登录</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <div class="formSet">
                    <h3>TripNow旅行计划定制</h3>
                    <el-divider></el-divider>
                    <el-form :model="planForm" :rules="rules" status-icon ref="planForm" class="demo-planForm"
                        id="labelColor">
                        <el-form-item label="标签" prop="interest">
                            <el-select v-model="planForm.interest" multiple placeholder="请选择">
                                <el-option :label="'城市观光'" value="cityScene"></el-option>
                                <el-option :label="'澳门景点'" value="macauSpot"></el-option>
                                <el-option :label="'历史人文'" value="hisCulture"></el-option>
                                <el-option :label="'主题公园'" value="amusePark"></el-option>
                                <el-option :label="'自然风光'" value="naturalSight"></el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="预计人数" prop="number">
                            <el-radio-group v-model="planForm.number" @change="printValue">
                                <el-radio :label="'1'">一人游</el-radio>
                                <el-radio :label="'2'">双人游</el-radio>
                                <el-radio :label="'3'">三人行</el-radio>
                                <el-radio :label="'4'">其他</el-radio>
                            </el-radio-group>
                            <el-input v-model="planForm.otherNumber" v-if="planForm.number == '4'"
                                style="width:120px; margin-left: 10px;" placeholder="请输入内容">
                            </el-input>
                        </el-form-item>
                        <el-form-item>
                            <el-button type="primary" @click="submitForm('planForm')">提交</el-button>
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
                if (value == '4') {
                    if (this.planForm.otherNumber == '') {
                        callback(new Error('请决定出行人数！'))
                    } else {
                        if (!(/^[+]{0,1}(\d+)$|^[+]{0,1}(\d+\.\d+)$/).test(this.planForm.otherNumber)) {
                            callback(new Error('请输入数字值'))
                        } else {
                            callback()
                        }
                    }
                } else {
                    callback()
                }
            }

            return {
                planForm: {
                    interest: [],
                    number: '',
                    otherNumber: '',
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
            }
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
        background-image: url(../assets/ZHimg/night.jpg);
        background-size: cover;
        color: #333;
        text-align: center;
        line-height: 40px;
        padding-top: 100px;
        padding-bottom: 100px;
    }

    .el-divider {
        background-color: #ffffff;
    }

    #labelColor>>>.el-form-item__label {
        color: #000000;
        font-size: 14px;
    }

    .formSet {
        width: 600px;
        background-color: rgb(255, 255, 255, 0.8);
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