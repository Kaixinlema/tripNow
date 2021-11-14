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
                    <el-form :model="planForm" status-icon ref="planForm" class="demo-planForm">
                        <el-form-item label="标签" prop="likedLabel">
                            <el-select v-model="planForm.interest" multiple placeholder="请选择">
                                <el-option label="城市观光" value="cityScene"></el-option>
                                <el-option label="购物商圈" value="shopMall"></el-option>
                                <el-option label="历史人文" value="hisCulture"></el-option>
                                <el-option label="美食汇集" value="foodTaste"></el-option>
                                <el-option label="休闲时光" value="relaxTime"></el-option>
                                <el-option label="主题世界" value="amusePark"></el-option>
                                <el-option label="自然风光" value="naturalSight"></el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="预计日开销" prop="predictCost">
                            <el-radio-group v-model="planForm.cost">
                                <el-radio :label="1">300元</el-radio>
                                <el-radio :label="2">600元</el-radio>
                                <el-radio :label="3">900元</el-radio>
                                <el-radio :label="4">其他</el-radio>
                            </el-radio-group>
                            <el-input v-model="planForm.otherCost" v-if="planForm.cost == 4"
                                style="width:120px; margin-left: 10px;" placeholder="请输入内容">
                            </el-input>
                        </el-form-item>
                        <el-form-item label="预计人数" prop="number">
                            <el-radio-group v-model="planForm.number">
                                <el-radio :label="1">一人游</el-radio>
                                <el-radio :label="2">双人游</el-radio>
                                <el-radio :label="3">三人行</el-radio>
                                <el-radio :label="4">其他</el-radio>
                            </el-radio-group>
                            <el-input v-model="planForm.otherNumber" v-if="planForm.number == 4"
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
            return {
                planForm: {
                    interest: [],
                    cost: 1,
                    otherCost: '',
                    number: 1,
                    otherNumber: '',
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
        width: 600px;
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