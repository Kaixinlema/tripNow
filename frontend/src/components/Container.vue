<template>
    <div>
        <el-container>
            <el-header style=" line-height: 60px;">
                <el-row>
                    <el-col :span="12" style="text-align: left;">
                        <el-button type="plain">图标</el-button>
                    </el-col>
                    <el-col :span="12" style="text-align: right;">
                        <el-button type="plain" @click="toLogin">登录</el-button>
                        <el-button type="plain" @click="toRegister">注册</el-button>
                    </el-col>
                </el-row>
            </el-header>
            <el-main>
                <el-row :gutter="20">
                    <el-col :span="12">
                        <div class="grid-content bg-purple">
                            <el-carousel height="400px">
                                <el-carousel-item v-for="item in imgs" :key="item.name">
                                    <el-image :src="item.img"></el-image>
                                </el-carousel-item>
                            </el-carousel>
                        </div>
                    </el-col>
                    <el-col :span="12">
                        <div class="grid-content bg-purple-light">
                            <el-carousel height="400px">
                                <el-carousel-item v-for="item in imgs" :key="item.name">
                                    <el-image :src="item.img"></el-image>
                                </el-carousel-item>
                            </el-carousel>
                        </div>
                    </el-col>
                </el-row>
                <div style="padding: 50px;">
                    <el-button type="primary" @click="toPlan">开始制定计划！</el-button>
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
    import img1 from "../assets/ZHimg/spring.jpg";
    import img2 from "../assets/ZHimg/summer.jpg";
    import img3 from "../assets/ZHimg/fall.jpg";
    import img4 from "../assets/ZHimg/winter.jpg";


    export default {
        name: "Container",
        data() {
            return {
                imgs: [
                    { img: img1, name: 'spring' },
                    { img: img2, name: 'summer' },
                    { img: img3, name: 'fall' },
                    { img: img4, name: 'winter' },
                ]
            };
        },
        methods: {
            toLogin() {
                this.$router.push("/login");
            },
            toRegister() {
                this.$router.push("/register");
            },
            toPlan() {
                this.$router.push("/plan");
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
    }

    .el-carousel__item h3 {
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        line-height: 200px;
        margin: 0;
    }

    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }

    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }
</style>