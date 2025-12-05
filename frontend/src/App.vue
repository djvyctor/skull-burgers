<script setup>
import { ref } from 'vue';

const view = ref('landing');
const products = ref([]);

const fetchMenu = async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/products');
    const data = await response.json();

    products.value = data;
    view.value = 'menu';
  } catch (error) {
    console.error("Erro ao buscar cardápio:", error);
    alert("A cozinha está fechada! (Erro de conexão)");
  }
};
</script>

<template>
  <div class="min-h-screen bg-black text-white font-pixel p-4 flex flex-col items-center">
    
    <div v-if="view === 'landing'" class="flex flex-col items-center justify-center h-[80vh] w-full max-w-lg border-4 border-white p-6 text-center">
      <h1 class="text-4xl font-bold mb-4 text-yellow-400 animate-pulse">
        SKULL BURGERS
      </h1>
      <p class="text-lg mb-8">A melhor lanchonete do subsolo.</p>
      
      <button 
        @click="fetchMenu"
        class="bg-black border-2 border-white px-6 py-3 hover:bg-white hover:text-black transition-colors font-bold text-xl cursor-pointer uppercase"
      >
        Ver Cardápio
      </button>
    </div>

    <div v-else class="w-full max-w-2xl animate-fade-in">
      <h2 class="text-3xl text-center mb-8 border-b-2 border-white pb-2">MENU</h2>
      
      <div class="space-y-6">
        <div 
          v-for="item in products" 
          :key="item.id" 
          class="border-2 border-gray-700 p-4 flex flex-col gap-2 hover:border-yellow-400 transition-colors"
        >
          <div class="flex justify-between items-center">
            <h3 class="text-xl font-bold text-yellow-400">{{ item.name }}</h3>
            <span class="text-lg">R$ {{ item.price.toFixed(2) }}</span>
          </div>
          <p class="text-gray-400 text-sm">{{ item.description }}</p>
          
          <button class="mt-2 bg-gray-900 text-xs py-2 border border-gray-600 hover:bg-white hover:text-black hover:border-white w-full uppercase">
            Adicionar ao Carrinho
          </button>
        </div>
      </div>

      <button @click="view = 'landing'" class="mt-8 text-sm text-gray-500 hover:text-white underline w-full text-center">
        Voltar ao início
      </button>
    </div>

  </div>
</template>

<style scoped>
/* Estilos específicos */
</style>