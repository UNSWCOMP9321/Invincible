<template>

    <transition enter-active-class="animated zoomIn" leave-active-class="animated zoomOut">
        <div class="content">
            <h1>First Demo</h1>
            <input class="input_bar" type="text" @keyup="test_input" v-model="city_name">

            <button class="btn btn-primary" @click="city_push">Input</button>
            <ul id="city_list">
                <!--<li v-for="item in citys" @click="delete_city">{{item}}</li>-->
                <li v-for="item in citys" @click="delete_city">{{item.name}}</li>
            </ul>
            <button class="btn btn-success input_button" @click="show_au">AU</button>
            <button class="btn btn-danger input_button2" @click="show_map">US</button>
            <br>
            <div id="city_content">{{city_name}}</div>
            <div id="picture" style="width: 100%;height: 600px"></div>
            <div id="picture_2" style="width: 100%;height: 600px"></div>
            <!--<img src="https://www.excel-easy.com/smi/examples/line-chart.png" alt="">-->
            <button @click="testb()">TEST</button>
            <div>{{str}}</div>
        </div>
    </transition>
</template>