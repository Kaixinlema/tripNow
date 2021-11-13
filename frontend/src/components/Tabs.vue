<template>
    <div>
        <el-form :model="choiceForm" ref="choiceForm">
            <el-tabs :tab-position="'left'" style="height: 100%;">
                <el-tab-pane :model="chosenLabels" v-for="(chosenLabel) in chosenLabels" :key="chosenLabel.value"
                    :label="chosenLabel.name">
                    <el-row>
                        <el-col :span="12" :model="items" v-for="(item) in items" :key="item.index">
                            <div v-if="item.itsLabel == chosenLabel.value" style="margin: 10px;">
                                <el-card :body-style="{ padding: '10px', margin: '10px', height: '400px'}">
                                    <el-scrollbar>
                                        <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                                            class="image">
                                        <div style="padding: 14px;">
                                            <h3>{{item.name}}</h3>
                                            <span style="text-align: left;">{{item.message}}</span>
                                            <div class="bottom clearfix">
                                            </div>
                                            <el-checkbox :label="item.index" :border="true" :model="item.ifSelected"
                                                @change="changeInfo(item.index)">
                                            </el-checkbox>
                                        </div>
                                    </el-scrollbar>
                                </el-card>
                            </div>
                        </el-col>
                    </el-row>
                </el-tab-pane>
            </el-tabs>
            <el-form-item>
                <el-button type="primary" @click.prevent="submitForm()">提交</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                choiceForm: {
                    finalChoice: [],
                },
                chosenLabels: [
                    { value: 'hisCulture', name: '人文古迹' },
                    { value: 'amusePark', name: '主题乐园' },
                    { value: 'cityScene', name: '城市观光' },
                    { value: 'extraRec', name: '相关推荐' },
                ],
                items: [
                    { name: 'chilong', index: 1, message: 'chilong-intro', itsLabel: 'amusePark', ifSelected: false },
                    { name: 'yunv', index: 2, message: 'yunv-intro', itsLabel: 'cityScene', ifSelected: false },
                    { name: 'ymy', index: 3, message: 'ymy-intro', itsLabel: 'hisCulture', ifSelected: false },
                    { name: 'huitong', index: 4, message: 'haha-intro', itsLabel: 'hisCulture', ifSelected: false },
                ],
            };
        },
        methods: {
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
    };
</script>