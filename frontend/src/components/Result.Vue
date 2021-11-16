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
                <h3>生成推荐结果</h3>
                <el-divider></el-divider>
                <el-row :gutter="10">
                    <el-col :span="16">
                        <baidu-map class="map" :center="map.center" :zoom="map.zoom" @ready="handler">
                            <!--缩放-->
                            <bm-navigation anchor="BMAP_ANCHOR_TOP_LEFT"></bm-navigation>
                            <!--定位-->
                            <bm-geolocation anchor="BMAP_ANCHOR_BOTTOM_RIGHT" :showAddressBar="true"
                                :autoLocation="true">
                            </bm-geolocation>
                            <!--点-->
                            <bm-marker :position="map.center" :dragging="map.dragging" animation="BMAP_ANIMATION_DROP">
                                <!--提示信息-->
                                <bm-info-window :show="map.show">中国·珠海</bm-info-window>
                            </bm-marker>
                        </baidu-map>
                    </el-col>
                    <el-col :span="8">
                        <el-card>
                            <h4>已选择景点及酒店</h4>
                            <el-divider></el-divider>
                        </el-card>
                    </el-col>
                </el-row>


                <h3>其他相关推荐</h3>
                <el-divider></el-divider>
                <el-form :model="resultForm" ref="resultForm">
                    <el-row>
                        <div class="scrollbarTry">
                            <el-col :span="6" :model="items" v-for="(item) in items" :key="item.index">
                                <div style="margin: 10px;">
                                    <el-card :body-style="{ padding: '10px', margin: '10px', height: '400px'}">
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
                        </div>
                    </el-row>
                    <el-form-item style="text-align: center; margin-top: 20px;">
                        <el-button type="primary" @click.prevent="submitForm()">提交</el-button>
                    </el-form-item>
                </el-form>
            </el-main>
        </el-container>


    </div>
</template>

<script>
    export default {
        name: "Result",

        data() {
            return {
                resultForm: {

                },
                map: {
                    center: { lng: 113.552724, lat: 22.255899 },
                    zoom: 15,
                    show: true,
                    dragging: true
                },
                items: [
                    { name: 'chilong', index: 1, message: 'chilong-intro', itsLabel: 'amusePark', ifSelected: false },
                    { name: 'yunv', index: 2, message: 'yunv-intro', itsLabel: 'cityScene', ifSelected: false },
                    { name: 'ymy', index: 3, message: 'ymy-intro', itsLabel: 'hisCulture', ifSelected: false },
                    { name: 'huitong', index: 4, message: 'haha-intro', itsLabel: 'hisCulture', ifSelected: false },
                    { name: 'huitong', index: 4, message: 'haha-intro', itsLabel: 'hisCulture', ifSelected: false },
                ],
            }
        },

        methods: {
            handler({ BMap, map }) {
                let me = this;
                console.log(BMap, map)
                // 鼠标缩放
                map.enableScrollWheelZoom(true);
                // 点击事件获取经纬度
                map.addEventListener('click', function (e) {
                    console.log(e.point.lng, e.point.lat)
                })
            },
            submitForm(event) {
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

    .map {
        width: 100%;
        height: 500px;
        margin-bottom: 30px;
    }

    .scrollbarTry {
        width: 100%;
        justify-content: space-between;
        white-space: nowrap;
        overflow-y: hidden;
        overflow-x: scroll;
        display: flex;
    }
</style>