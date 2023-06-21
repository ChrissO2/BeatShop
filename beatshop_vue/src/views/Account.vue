<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My account</h1>
            </div>

            <hr>
            
            <div class="column is-12">
                <h2 class="subtitle">My orders</h2>

                <div v-if="orders.length">
                    <OrderSummary
                    v-for="order in orders"
                    v-bind:key="order.id"
                    v-bind:order="order" />
                </div>

                <div v-else>
                    <p>You don't have any orders, go to <a href="/">homepage</a> to buy something</p>
                </div>

                
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import OrderSummary from '@/components/OrderSummary.vue'

export default {
    name: 'Account',
    components: {
        OrderSummary
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'My account | BestStore'

        this.getMyOrders()
    },
    methods: {
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>