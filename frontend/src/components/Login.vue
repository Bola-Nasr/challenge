<template>
  <div class="bg-white p-6 rounded-lg shadow-md">
    <h2 class="text-xl font-semibold mb-4">W&D Property Management Login</h2>
    <div class="space-y-4">
      <input v-model="username" type="text" placeholder="Username" class="w-full p-3 border rounded-lg" />
      <input v-model="password" type="password" placeholder="Password" class="w-full p-3 border rounded-lg" />
      <button @click="login" class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700">Login</button>
    </div>
  </div>
</template>

<script>
import { login } from '../services/api';

export default {
  data() {
    return { username: 'admin', password: 'admin' };
  },
  methods: {
    async login() {
      try {
        const token = await login(this.username, this.password);
        this.$emit('login-success', token);
      } catch (error) {
        alert('Login failed. Please check your credentials.');
      }
    },
  },
};
</script>