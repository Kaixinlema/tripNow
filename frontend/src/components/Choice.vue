<template>
    <div>
        <transition name="fade">
            <Loading v-if="isLoading"></Loading>
        </transition>
        <el-container>
            <el-header style=" line-height: 60px;">
                <el-row>
                    <el-col :span="12" style="text-align: left;">
                        <el-button type="plain">图标</el-button>
                        <el-button type="plain" @click="toIndex">首页</el-button>
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
                    <h3>选择详细景点</h3>
                    <el-divider></el-divider>
                    <el-form :model="choiceForm" ref="choiceForm">
                        <el-row>
                            <el-col :span="20">
                                <el-tabs :tab-position="'left'" style="height: 100%;">
                                    <el-tab-pane :model="labels" v-for="(labelIndex) in labels"
                                        :key="labelIndex" :label="allLabels[labelIndex-1].name">
                                        <el-row>
                                            <el-col :span="12" :model="items" v-for="(item) in items" :key="item.index">
                                                <div v-if="item.itsLabel == labelIndex" style="margin: 10px;">
                                                    <el-card
                                                        :body-style="{ padding: '10px', margin: '10px', height: '400px'}">
                                                        <el-scrollbar>
                                                            <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                                                                class="image">
                                                            <div style="padding: 14px;">
                                                                <span style="font-size: 20px;">{{item.name}}</span>
                                                                <div style="float: right; display: inline;">
                                                                    <el-checkbox label="我想去" :border="true"
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
                                    <h4>已选择景点</h4>
                                <el-divider></el-divider>
                                <div v-if="choiceForm.finalChoice.length > 0" class="emptySet">
                                    <div v-for="index in choiceForm.finalChoice">
                                        <span>{{items[index].name}}</span>
                                    </div>
                                </div>
                                <div v-else="choiceForm.finalChoice.length == 0" class="emptySet">
                                    <span>暂无数据</span></span>
                                </div>

                                    <div style="text-align: center;">
                                        <el-form-item>
                                            <el-button type="primary" @click.prevent="submitForm('choiceForm')">提交</el-button>
                                        </el-form-item>
                                    </div>
                                </el-card>
                            </el-col>
                        </el-row>
                    </el-form>
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>
import axios from 'axios';
import Loading from '../components/loading'

    export default {
        components:{ Loading },
        name: "Choice",
        data() {
            return {
                choiceForm: {
                    username: '',
                    finalChoice: [],
                },
                items: [
                    { name: '珠海长隆海洋王国', index: 0, 
                    message: '长隆海洋王国位于珠海横琴长隆国际海洋度假区，呈献世界最大的水族馆之一，让您一次过与珍稀的鲸鲨、白鲸、北极熊和其它可爱动物见面！这个世界级主题公园更荣获由主题娱乐协会(TEA) 颁发2014年度唯一的主题公园「杰出成就奖」，是您不可错过的必游景点！', 
                    itsLabel: 4, ifSelected: false },
                    { name: '珠海渔女', index: 1, 
                    message: '珠海的地标性建筑，拍一张游客纪念照，逛逛附近的海滨公园和情侣路。', 
                    itsLabel: 1, ifSelected: false },
                    { name: '情侣路', index: 2, 
                    message: '珠海的城市名片，漫步海边，欣赏珠海渔女雕像。', 
                    itsLabel: 1, ifSelected: false },
                    { name: '圆明新园', index: 3, 
                    message: '按照1:1比例仿圆明园建造，感受小皇家园林的恢弘气势，观看顶级特效表演。', 
                    itsLabel: 3, ifSelected: false },
                    { name: '海滨公园', index: 4, 
                    message: '距离市区最近的海岛，散步爬山，在海风的吹拂下看日出日落。', 
                    itsLabel: 4, ifSelected: false },
                    { name: '东澳岛', index: 5, 
                    message: '爬斧担山登高望远，在南沙湾戏水游泳，看摩崖石刻、烽火台、铳城等历史遗迹。', 
                    itsLabel: 5, ifSelected: false },
                    { name: '外伶仃岛', index: 6, 
                    message: '广东可看见香港市区的海岛，游山玩水吃海鲜，享受悠闲度假时光。', 
                    itsLabel: 5, ifSelected: false },
                    { name: '港珠澳大桥', index: 7, 
                    message: '中国境内一座连接香港、珠海和澳门的桥隧工程。可以去打卡。', 
                    itsLabel: 1, ifSelected: false },
                    { name: '九洲岛', index: 8, 
                    message: '离市区仅需15分钟船程的海岛，在沙滩上散步吹风吃烧烤，欣赏天然石景。', 
                    itsLabel: 5, ifSelected: false },
                    { name: '淇澳岛', index: 9, 
                    message: '在木栈道上骑行，参观沙湾古遗址、白石街等古迹，冬季去红树林湿地保护区观鸟。', 
                    itsLabel: 5, ifSelected: false },
                    { name: '野狸岛', index: 10, 
                    message: '距离市区最近的海岛，散步爬山，在海风的吹拂下看日出日落。', 
                    itsLabel: 5, ifSelected: false },
                    { name: '珠海市博物馆', index: 11, 
                    message: '古典风格的地标建筑，展品丰富，可以了解珠海本地的文化和历史。', 
                    itsLabel: 3, ifSelected: false },
                    { name: '景山公园', index: 12, 
                    message: '乘坐石景山索道，登上山顶，俯瞰壮观的山海风光。', 
                    itsLabel: 4, ifSelected: false },
                    { name: '澳门塔', index: 13, 
                    message: '澳门地标，可以登上塔顶一览整个澳门的风光。', 
                    itsLabel: 2, ifSelected: false },
                    { name: '大三巴牌坊', index: 14, 
                    message: '澳门最具代表性的名胜古迹，澳门八景之一，位于澳门炮台山下，左临澳门博物馆和大炮台名胜。', 
                    itsLabel: 2, ifSelected: false },
                    { name: '澳门渔人码头', index: 15, 
                    message: '澳门最具代表性的名胜古迹，澳门八景之一，位于澳门炮台山下，左临澳门博物馆和大炮台名胜。', 
                    itsLabel: 2, ifSelected: false },

                ],
                allLabels: [
                    { value: 1, name: '城市观光' },
                    { value: 2, name: '澳门景点' },
                    { value: 3, name: '历史人文' },
                    { value: 4, name: '主题公园' },
                    { value: 5, name: '自然风光' },
                ],
                labels: [],
                number: '',
                username: '',
                isLoading: false,
            }
        },
        methods: {
            toRegister() {
                this.$router.push("register");
            },
            toLogin() {
                this.$router.push("login");
            },
            toIndex() {
                this.$router.push("/");
            },
            changeInfo(e) {
                console.log(e);
                this.items[e].ifSelected = !this.items[e].ifSelected;
                if (this.items[e].ifSelected) {
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
            submitForm(formName) {
                const path = 'http://127.0.0.1:5000/choice';
                let formData = new FormData;
                formData.append("choice", this.choiceForm.finalChoice);
                this.isLoading = true;
                // console.log(formData.get("choice"));
                axios.post(path,{
                    choices: this.choiceForm.finalChoice, 
                }).then((res)=>{
                    console.log(res.data);
                    this.isLoading = false;
                    this.$message.success("为您推荐以下路线：）")
                    this.$router.push({
                        name: 'plan', 
                        params: {
                            route: res.data,
                            number: this.number
                        }
                    })

                })

            },
        },
        created() {
            this.labels = this.$route.params.labels;
            this.number = this.$route.params.number;
            let curr_user = sessionStorage.getItem('accessToken')
            if (curr_user) {
                this.username = JSON.parse(curr_user)
            }
        }
    }
</script>

<style scoped>
    .fade-enter,
    .fade-leave-active {
        opacity: 0;
    }
    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.5s;
    }
    .el-header {
        background-color: #ffffff;
        color: #333;
        border-radius: 1px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }

    .el-main {
        background-color: #E9EEF3;
        color: #333;
    }

    .el-card .el-scrollbar {
        height: 100%;
    }

    .el-card .el-scrollbar__wrap {
        overflow: scroll;
        overflow-x: hidden;
    }

    .formSet {
        width: 90%;
        background-color: #ffffff;
        border-radius: 5px;
        margin: auto;
        padding: 20px;
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