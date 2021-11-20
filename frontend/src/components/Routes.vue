<template>
    <div>
        <transition name="fade">
            <Loading v-if="isLoading"></Loading>
        </transition>
        <el-container>
            <el-header style=" line-height: 60px;">
                <el-row>
                    <el-col :span="12" style="text-align: left;">
                        <div class="headIcon" @click="$router.push('/')">
                        </div>
                    </el-col>
                    <el-col v-if="username == ''" :span="12" style="text-align: right;">
                        <el-button type="danger" @click="toLogin"> 登录 </el-button>
                        <el-button type="danger" @click="toRegister">注册</el-button>
                    </el-col>
                    <el-col v-else :span="12" style="text-align: right;">
                        <el-a style="color:grey; font-size:20px; margin-right: 20px;">
                            <i class="el-icon-user-solid"></i>
                            <b> {{username}} </b>
                        </el-a>
                        <el-button type="text" icon="el-icon-switch-button" @click="logout" plain>退出登录</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <h3>推荐路线：</h3>
                <el-divider></el-divider>
                <el-row :gutter="10">
                    <el-col :span="12">
                        <baidumap v-bind:points="this.points"></baidumap>
                    </el-col>
                    <!-- 这里新加了侧栏显示推荐简介 -->
                    <el-col :span="12">
                        <el-card>
                            <h3>行程概要</h3>
                            <el-divider></el-divider>
                            <div class="showResult">
                                <el-row style="padding: 5px;">
                                    <el-tag type="danger" style="font-size: 12px; font-weight:bold;">已选目的城市</el-tag>
                                    <span v-if="this.macau==1"> 珠海、澳门</span>
                                    <span v-if="this.macau==0"> 珠海 </span>
                                </el-row>
                                <el-row style="padding: 5px;">
                                    <el-tag type="danger" style="font-size: 12px; font-weight:bold;">选择游玩景点 </el-tag>
                                        <span v-for="aRoute in this.route">{{ aRoute["attraction_name"] }} </span>
                                </el-row>
                                <el-row style="padding: 5px;">
                                    <el-tag type="danger" style="font-size: 12px; font-weight:bold;">推荐酒店</el-tag>
                                        <span v-for="hotel in this.hotels">{{ hotel["name"] }} </span>
                                </el-row>
                                <el-row style="padding: 5px;">
                                    <el-tag type="danger" style="font-size: 12px; font-weight:bold;">推荐游玩天数</el-tag>
                                    <span>预计{{this.numofday}}天</span>
                                </el-row>
                                <el-row style="padding: 5px;">
                                    <el-tag type="danger" style="font-size: 12px; font-weight:bold;">预计开销估算</el-tag>
                                    <span>预计人均 ¥{{this.cost}}</span>
                                </el-row>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>

                <!-- 这里动态显示每天的行程 -->
                <el-row>
                    <el-col :span="6">
                        <el-steps direction="vertical" :active="day.length" style="margin-bottom: 50px;">
                            <el-step v-for="(count, index) in this.numofday" :key="index" :title="'day '+count">
                                <template slot="description">
                                    <el-card style="width: 800px; margin: 10px;">
                                        <p style="font-size: 18px; font-weight: bold;">
                                            <i class="el-icon-s-flag"></i>
                                            游玩景点：</p>
                                        <span v-for="poi in day" v-if="poi['day']==count">
                                              <p style="font-weight: bold; font-size: 16px; color: orange;"> 
                                                   <i class="el-icon-place"></i> 
                                                  {{ poi['attraction']["attraction_name"] }} </p>
                                              <p style=" font-size: 14px;">   {{ poi['attraction']['attraction_detail']}} </p>
                                        </span>
                                         <p style="font-size: 16px; font-weight: bold;">
                                            <i class="el-icon-s-home"></i>
                                            推荐住宿酒店：
                                         </p>
                                        <span v-if="hotels[index]">
                                            <p style="font-weight: bold; font-size: 16px; color: orange;"> 
                                                 <i class="el-icon-location-information"></i>
                                                {{hotels[index]['name']}} 
                                            </p>
                                            <p style=" font-size: 14px;"> 价格：¥{{hotels[index]['price']}}起每晚</p>
                                            <p style=" font-size: 14px;"> 评分：{{hotels[index]['score']}}/5.0 </p>
                                            <p style=" font-size: 14px;">距离{{items[hotels[index]['attraction_id']].name}} {{hotels[index]['distance']}}</p>
                                        </span>
                                    </el-card>
                                </template>
                            </el-step>
                        </el-steps>
                    </el-col>
                </el-row>

                <!-- 这里开始有表单内容 -->
                <h3>其他相关推荐</h3>
                <el-divider></el-divider>
                <el-form :model="resultForm" ref="resultForm">
                    <div class="scrollbarTry">
                        <!-- 改成div之后就可以缩起来了 -->
                        <!-- 这里的结构和choice里面的完全复用了 -->
                        <div class="scrollBar" :model="recommend" v-for="(idx) in this.recommend" :key="idx">
                            <div style="margin: 10px;">
                                <el-card :body-style="{ padding: '10px', margin: '10px', height: '400px'}">
                                    <el-scrollbar>
                                        <el-carousel height="180px" width="320px">
                                            <el-carousel-item v-for=" (index) in imgGroup.slice((idx)*4, (idx+1)*4)"
                                                :key="index">
                                                <img :src="index" class="image" style="width:320px; height: 180px">
                                            </el-carousel-item>
                                        </el-carousel>
                                        <div style="padding: 14px;">
                                            <span style="font-size: 20px;">{{items[idx].name}}</span>
                                            <!-- 点了之后就会存进resultform里面的addChoice数组 -->
                                            <div style="float: right; display: inline;">
                                                <el-checkbox label="我想去" :border="true" :model="items[idx].ifSelected"
                                                    size="medium" @change="changeInfo(items[idx].index)">
                                                </el-checkbox>
                                            </div>
                                            <el-divider></el-divider>
                                            <span style="text-align: left;">{{items[idx].message}}</span>
                                            <div class="bottom clearfix">
                                            </div>
                                        </div>
                                    </el-scrollbar>
                                </el-card>
                            </div>
                        </div>
                    </div>

                    <el-form-item style="text-align: center; margin-top: 20px;">
                        <el-button type="primary" @click="submitForm()">重新规划</el-button>
                    </el-form-item>
                </el-form>
            </el-main>
        </el-container>


    </div>
</template>

<script>
    import BaiduMap from '../components/baidumap';
    import axios from 'axios';
    import Loading from '../components/loading'

    const _ = require("lodash")
    const frames = []
    _.times(64, v => {
        frames.push(require(`../assets/attractImg/${v}.jpeg`))
    })

    export default {
        inject: ['reload'],
        name: "Routes",
        components: {
            "baidumap": BaiduMap,
            Loading
        },
        data() {
            return {
                resultForm: {
                    addChoice: [],
                },
                items: [
                    {
                        name: '珠海长隆海洋王国', index: 0,
                        message: '长隆海洋王国位于珠海横琴长隆国际海洋度假区，呈献世界最大的水族馆之一，让您一次过与珍稀的鲸鲨、白鲸、北极熊和其它可爱动物见面！这个世界级主题公园更荣获由主题娱乐协会(TEA) 颁发2014年度唯一的主题公园「杰出成就奖」，是您不可错过的必游景点！',
                        itsLabel: 4, ifSelected: false, 
                    },

                    {
                        name: '珠海渔女', index: 1,
                        message: '珠海的地标性建筑，拍一张游客纪念照，逛逛附近的海滨公园和情侣路。',
                        itsLabel: 1, ifSelected: false,
                    },

                    {
                        name: '情侣路', index: 2,
                        message: '珠海的城市名片，漫步海边，欣赏珠海渔女雕像。',
                        itsLabel: 1, ifSelected: false,
                    },

                    {
                        name: '圆明新园', index: 3,
                        message: '按照1:1比例仿圆明园建造，感受小皇家园林的恢弘气势，观看顶级特效表演。',
                        itsLabel: 3, ifSelected: false,
                    },

                    {
                        name: '海滨公园', index: 4,
                        message: '距离市区最近的海岛，散步爬山，在海风的吹拂下看日出日落。',

                        itsLabel: 4, ifSelected: false,
                    },
                    {
                        name: '东澳岛', index: 5,
                        message: '爬斧担山登高望远，在南沙湾戏水游泳，看摩崖石刻、烽火台、铳城等历史遗迹。',
                        itsLabel: 5, ifSelected: false,
                    },

                    {
                        name: '外伶仃岛', index: 6,
                        message: '广东可看见香港市区的海岛，游山玩水吃海鲜，享受悠闲度假时光。',
                        itsLabel: 5, ifSelected: false,
                    },

                    {
                        name: '港珠澳大桥', index: 7,
                        message: '中国境内一座连接香港、珠海和澳门的桥隧工程。可以去打卡。',
                        itsLabel: 1, ifSelected: false,
                    },

                    {
                        name: '九洲岛', index: 8,
                        message: '离市区仅需15分钟船程的海岛，在沙滩上散步吹风吃烧烤，欣赏天然石景。',
                        itsLabel: 5, ifSelected: false,
                    },

                    {
                        name: '淇澳岛', index: 9,
                        message: '在木栈道上骑行，参观沙湾古遗址、白石街等古迹，冬季去红树林湿地保护区观鸟。',
                        itsLabel: 5, ifSelected: false,
                    },

                    {
                        name: '野狸岛', index: 10,
                        message: '距离市区最近的海岛，散步爬山，在海风的吹拂下看日出日落。',
                        itsLabel: 5, ifSelected: false,price: 0,
                    },

                    {
                        name: '珠海市博物馆', index: 11,
                        message: '古典风格的地标建筑，展品丰富，可以了解珠海本地的文化和历史。',
                        itsLabel: 3, ifSelected: false,
                    },

                    {
                        name: '景山公园', index: 12,
                        message: '乘坐石景山索道，登上山顶，俯瞰壮观的山海风光。',
                        itsLabel: 4, ifSelected: false, 
                    },

                    {
                        name: '澳门塔', index: 13,
                        message: '澳门地标，可以登上塔顶一览整个澳门的风光。',
                        itsLabel: 2, ifSelected: false,
                    },

                    {
                        name: '大三巴牌坊', index: 14,
                        message: '澳门最具代表性的名胜古迹，澳门八景之一，位于澳门炮台山下，左临澳门博物馆和大炮台名胜。',
                        itsLabel: 2, ifSelected: false,
                    },

                    {
                        name: '澳门渔人码头', index: 15,
                        message: '澳门最具代表性的名胜古迹，澳门八景之一，位于澳门炮台山下，左临澳门博物馆和大炮台名胜。',
                        itsLabel: 2, ifSelected: false,
                    },

                ],
                day: [],
                imgGroup: frames,
                username: '',
                route: [],
                recommend: [],
                points: [],
                hotels: [],
                isLoading: false,
                macau: false,
                numofday: '',
                cost: '',
            }
        },

        methods: {
            toLogin() {
                this.$router.push("/login");
            },
            toRegister() {
                this.$router.push("/register");
            },
            logout() {
                sessionStorage.removeItem("accessToken")
                this.$message.success("Logout Successful");
                this.reload();
            },
            changeInfo(e) {
                console.log(e);
                this.items[e].ifSelected = !this.items[e].ifSelected;
                if (this.items[e].ifSelected) {
                    this.resultForm.addChoice.push(e);
                } else {
                    var length = this.resultForm.addChoice.length;
                    for (var index = length - 1; index < length; index++) {
                        if (this.resultForm.addChoice[index] == e) {
                            this.resultForm.addChoice.splice(index, 1);
                        }
                    }
                }
                console.log(this.resultForm.addChoice);
            },

            submitForm() {
                function point(lng, lat) {
                    this.lng = lng;
                    this.lat = lat;
                }
                if(this.items[13].ifSelected==true || 
                   this.items[14].ifSelected==true ||
                   this.items[15].ifSelected==true){
                       this.macau = 1;
                }
                var new_recom = this.route.concat(this.resultForm.addChoice);
                const path = 'http://127.0.0.1:5000/choice';
                this.isLoading = true;
                axios.post(path, {
                    choices: new_recom,
                    type: this.type,
                }).then((res) => {
                    console.log(res.data);
                    this.isLoading = false;
                    this.$message.success("为您推荐以下路线及酒店 ：）")
                    this.route = res.data.route;
                    this.recommend = res.data.recommend;
                    this.day = res.data.day;
                    this.numofday = res.data.numofday;
                    this.hotels = res.data.hotel;
                    this.points = [];
                    for (let i = 0; i < this.route.length; i++) {
                        this.points.push(new point(this.route[i]['attraction_lng'], this.route[i]['attraction_lat']));
                    }
                    this.$nextTick(() => {
                        if (BaiduMap){
                            this.$refs.Baidumap;
                        }
                    })
                })
            }
        },
        created() {
            function point(lng, lat) {
                this.lng = lng;
                this.lat = lat;
            }
            this.route = this.$route.params.routes;
            console.log(this.route);
            this.recommend = this.$route.params.recommends;
            this.day = this.$route.params.days;
            console.log(this.day);0
            this.hotels = this.$route.params.hotels;
            console.log(this.hotels);
            this.macau = this.$route.params.macau;
            this.numofday = this.$route.params.numofday;
            this.type = this.$route.params.type;
            this.cost = this.$route.params.cost;
            for (let k = 0; k< this.day.length; k++){
                console.log(this.day[k]['day']);
                console.log(this.day[k]['attraction']['id']);
            }
            for (let i = 0; i < this.route.length; i++) {
                this.points.push(new point(this.route[i]["attraction_lng"], this.route[i]["attraction_lat"]));
            }
            let curr_user = sessionStorage.getItem('accessToken')
            if (curr_user) {
                this.username = JSON.parse(curr_user)
            }
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

    .headIcon {
        width: 150px;
        height: 60px;
        background-image: url(../assets/ZHimg/icon-black.png);
        background-size: cover;
    }

    .scrollbarTry {
        width: 100%;
        white-space: nowrap;
        overflow: scroll;
        overflow-y: hidden;
        overflow-x: scroll;
    }

    .scrollBar {
        width: 33%;
        display: inline-block;
    }

    .showResult {
        font-size: 14px;
    }

    .el-card .el-scrollbar {
        height: 100%;

    }

    .el-card .el-scrollbar__wrap {
        overflow-x: hidden;
        overflow-y: scroll;
    }
</style>