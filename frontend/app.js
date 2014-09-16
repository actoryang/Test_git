angular.module('y710', ['ngRoute',])

.config(function($routeProvider) {
    $routeProvider
     .when('/', {
        conroller: 'HomeCtrl',
        templateUrl: 'views/home.html'
     })
     .when('/login', {
        controller: 'LoginCtrl',
        templateUrl: 'views/login.html'
     })
     .when('/signup', {
        conroller: 'SignupCtrl',
        templateUrl: 'views/signup.html'
     })
     .when('/logout', {
        conroller: 'LogoutCtrl',
        templateUrl: null
     })
     .otherwise({
        redirectTo: '/'
     })
})