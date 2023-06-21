<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cart</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <CartItem
                            v-for="item in cart.items"
                            v-bind:key="item.id"
                            v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart"
                        />
                    </tbody>
                </table>

                <p v-else>You don't have any products in your cart...</p>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Summary</h2>

                <strong>${{ cartTotalPrice }}</strong>, {{ cartTotalLength }} products

                <hr>
                <div v-if="isUserLoggedIn && cartTotalLength > 0">
                    <router-link to="/cart/checkout" class="button is-dark mr-3">Proceed to checkout</router-link>
                </div>
                <div v-else-if="cartTotalLength === 0">
                    <router-link to="/" class="button is-dark mr-3">You don't have any products in your cart</router-link>
                </div>
                <div v-else>
                    <router-link to="/log-in" class="button is-dark mr-3">Log in to proceed to payment</router-link>
                </div>
                
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'
import { StripeElementCard } from '@vue-stripe/vue-stripe'
import { toast } from 'bulma-toast'

export default {
    name: 'Cart',
    components: {
        CartItem,
        StripeElementCard,
    },
    data() {
        return {
            cart: {
                items: []
            },
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
        this.auth = this.$store.state.isAuthenticated
    },
    methods: {
        removeFromCart(item) {
            this.$store.commit('removeFromCart', item)
            toast({
                message: 'Product was removed from the cart',
                type: 'is-danger',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.length;
        },
        cartTotalPrice() {
            let totalPrice = 0
            for (let i = 0; i < this.cart.items.length; i++) {
                totalPrice += parseFloat(this.cart.items[i].price)
            }
            return totalPrice.toFixed(2)
        },
        isUserLoggedIn() {
            return this.$store.state.isAuthenticated
        },
    }
}
</script>