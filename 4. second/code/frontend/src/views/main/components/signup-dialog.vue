<template>
  <el-dialog custom-class="signup-dialog" title="회원가입" v-model="state.dialogVisible" @close="handleClose">
    <el-form :model="state.form" :rules="state.rules" ref="signupForm" :label-position="state.form.align">
      <el-form-item prop="organization" label="소속" :label-width="state.formLabelWidth" >
        <el-input v-model="state.form.organization" autocomplete="off" maxlength="30"></el-input>
      </el-form-item>
      <el-form-item prop="role" label="직책" :label-width="state.formLabelWidth" >
        <el-input v-model="state.form.role" autocomplete="off" maxlength="30"></el-input>
      </el-form-item>
      <el-form-item prop="name" label="이름" :label-width="state.formLabelWidth" >
        <el-input v-model="state.form.name" autocomplete="off" maxlength="30"></el-input>
      </el-form-item>
      <el-form-item prop="id" label="아이디" :label-width="state.formLabelWidth" >
        <div style="display: flex; align-items: center;">
          <el-input v-model="state.form.id" autocomplete="off"></el-input>
          <el-button @click="duplicateCheck">중복체크</el-button>
        </div>
      </el-form-item>
      <el-form-item prop="password" label="비밀번호" :label-width="state.formLabelWidth">
        <el-input v-model="state.form.password" autocomplete="off" show-password></el-input>
      </el-form-item>
      <el-form-item prop="checkPassword" label="비밀번호확인" :label-width="state.formLabelWidth">
        <el-input v-model="state.form.checkPassword" autocomplete="off" show-password></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="clickSignup">가입하기</el-button>
      </span>
    </template>
  </el-dialog>
</template>
<style>
.signup-dialog {
  width: 400px !important;
  height: 500px;
}
.signup-dialog .el-dialog__headerbtn {
  float: right;
}
.signup-dialog .el-form-item__content {
  margin-left: 0 !important;
  float: right;
  width: 200px;
  display: inline-block;
  background-color:whitesmoke;
}
.signup-dialog .el-form-item {
  margin-bottom: 20px;
}
.signup-dialog .el-form-item__error {
  font-size: 12px;
  color: red;
}
.signup-dialog .el-input__suffix {
  display: none;
}
.signup-dialog .el-dialog__footer {
  margin: 0 calc(50% - 80px);
  padding-top: 0;
  display: inline-block;
}
.signup-dialog .dialog-footer .el-button {
  width: 120px;
}
</style>
<script>
import { reactive, computed, ref, onMounted, defineProps, defineEmits } from 'vue'
import { useStore } from 'vuex'

export default {
  name: 'signup-dialog',
  emits: ['closeSignupDialog'], // 이벤트 목록 선언

  props: {
    open: {
      type: Boolean,
      default: false
    }
  },

  setup(props, { emit }) {
    const store = useStore()
    const signupForm = ref(null)

    const state = reactive({
      form: {
        organization: '',
        role:'',
        id: '',
        password: '',
        checkPassword:'',
        align: 'left'
      },
      rules: {
        organization:[
          {required: false, message: 'Please keep it within 30 characters', trigger: 'blur'}
        ],
        role:[
          {required: false, message: 'Please keep it within 30 characters', trigger: 'blur'}
        ],
        name:[
          {required: true, message: 'Please input name within 30 characters', trigger: 'blur'}
        ],
        id: [
          { required: true, message: 'Please input ID', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please input password', trigger: 'blur' }
        ],
        checkPassword: [
          { required: true, message: 'Please input checkPassword', trigger: 'blur' }
        ]
      },
      dialogVisible: computed(() => props.open),
      formLabelWidth: '120px'
    })

    onMounted(() => {
      // console.log(signupForm.value)
    })

    const duplicateCheck = async function () {

    }

    const clickSignup = async function () {
      signupForm.value.validate(async (valid) => {
        if (valid) {
          console.log('submit');
          await store.dispatch('accountStore/signupAction', { id: state.form.id, password: state.form.password });
          console.log('accessToken ' + store.getters['accountStore/getToken']);
        } else {
          alert('Validate error!');
        }
      });
    }

    const handleClose = function () {
      state.form.id = ''
      state.form.password = ''
      emit('closeSignupDialog'); // 이벤트 발생
    }

    return { signupForm, state, clickSignup, handleClose, duplicateCheck }
  }
}
</script>
