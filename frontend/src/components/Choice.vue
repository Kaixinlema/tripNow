<template>
    <div>
        <el-container>
            <el-header style=" line-height: 60px;">
                <el-row>
                    <el-col :span="12" style="text-align: left;">
                        <div class="headIcon" @click="$router.push('/')">
                        </div>
                    </el-col>
                    <el-col :span="12" style="text-align: right;">
                        <el-button type="plain">用户名</el-button>
                        <el-button type="plain">退出登录</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <h3>选择详细景点</h3>
                <el-divider></el-divider>
                <el-form :model="choiceForm" ref="choiceForm">
                    <el-row>
                        <el-col :span="20">
                            <el-tabs :tab-position="'left'" style="height: 100%;">
                                <el-tab-pane :model="chosenLabels" v-for="(chosenLabel) in chosenLabels"
                                    :key="chosenLabel.value" :label="chosenLabel.name">
                                    <el-row>
                                        <el-col :span="12" :model="items" v-for="(item) in items" :key="item.index">
                                            <div v-if="item.itsLabel == chosenLabel.value" style="margin: 10px;">
                                                <el-card
                                                    :body-style="{ padding: '10px', margin: '10px', height: '400px'}">
                                                    <el-scrollbar>
                                                        <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                                                            class="image">
                                                        <div style="padding: 14px;">
                                                            <span style="font-size: 20px;">{{item.name}}</span>
                                                            <div style="float: right; display: inline;">
                                                                <el-checkbox :label="item.index" :border="true"
                                                                    :model="item.ifSelected" size="medium"
                                                                    @change="changeInfo(item.index)">
                                                                </el-checkbox>
                                                            </div>
                                                            <el-divider></el-divider>
                                                            <span style="text-align: left;">{{item.message}}</span>
                                                            <div class="bottom clearfix">
                                                            </div>
                                                        </div>
                                                    </el-scrollbar>
                                                </el-card>
                                            </div>
                                        </el-col>
                                    </el-row>
                                </el-tab-pane>
                            </el-tabs>
                        </el-col>
                        <el-col :span="4">
                            <el-card>
                                <div slot="header" class="clearfix">
                                    <span>已选择景点</span>
                                </div>
                                <!-- <ul>
                                        <li v-for="index in choiceForm.finalChoice">{{items[index-1].name}}</li>
                                    </ul> -->
                                <div style="text-align: center;">
                                    <el-form-item>
                                        <el-button type="primary" @click.prevent="submitForm()">提交</el-button>
                                    </el-form-item>
                                </div>
                            </el-card>
                        </el-col>
                    </el-row>
                </el-form>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "Choice",
        data() {
            return {
                choiceForm: {
                    username: '',
                    finalChoice: [],
                },
                items: [
                    { name: 'chilong', index: 1, message: 'chilong-intro', itsLabel: 'amusePark', ifSelected: false },
                    { name: 'yunv', index: 2, message: 'yunv-intro', itsLabel: 'cityScene', ifSelected: false },
                    { name: 'ymy', index: 3, message: 'ymy-intro', itsLabel: 'hisCulture', ifSelected: false },
                    { name: 'huitong', index: 4, message: 'haha-intro', itsLabel: 'hisCulture', ifSelected: false },
                ],
                chosenLabels: [
                    { value: 'hisCulture', name: '人文古迹' },
                    { value: 'amusePark', name: '主题乐园' },
                    { value: 'cityScene', name: '城市观光' },
                    { value: 'extraRec', name: '相关推荐' },
                ],
            }
        },
        methods: {
            toIndex() {
                this.$router.push("/");
            },
            changeInfo(e) {
                console.log(e);
                this.items[e - 1].ifSelected = !this.items[e - 1].ifSelected;
                if (this.items[e - 1].ifSelected) {
                    this.choiceForm.finalChoice.push(e);
                } else {
                    var length = this.choiceForm.finalChoice.length;
                    for (var index = 0; index < length; index++) {
                        if (this.choiceForm.finalChoice[index] == e) {
                            this.choiceForm.finalChoice.splice(index, 1);
                        }
                    }
                }
                console.log(this.choiceForm.finalChoice);
            },
            submitForm(event) {
                let formData = new FormData;
                formData.append("choice", this.choiceForm.finalChoice);
                console.log(formData.get("choice"));
                // this.$refs[formName].validate((valid) => {
                //     if (valid) {
                //         alert('submit!');
                //     } else {
                //         console.log('error submit!!');
                //         return false;
                //     }
                // });
            },
        }
    }
</script>

<style scoped>
    .el-header {
        background-color: #ffffff;
        color: #333;
        border-radius: 1px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }

    .el-main {
        background-color: white;
        color: #333;
        padding: 0px 20px 60px 40px;
    }

    .el-card .el-scrollbar {
        height: 100%;
    }

    .el-card .el-scrollbar__wrap {
        overflow: scroll;
        overflow-x: hidden;
    }

    .headIcon {
        width: 150px;
        height: 60px;
        background-image: url(../assets/ZHimg/icon-black.png);
        background-size: cover;
    }

    .setCard {
        width: 400px;
        margin: 10px;
    }

    .time {
        font-size: 13px;
        color: #999;
    }

    .bottom {
        margin-top: 13px;
        line-height: 12px;
    }

    .image {
        width: 50%;
        display: block;
        margin: auto;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both
    }
</style>