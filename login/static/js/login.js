var loginApp = angular.module('loginApp', []);
loginApp.controller('LoginCtrl', ['$scope','$http','$log', function($scope,$http,$log) {
  $scope.error = ""
  $scope.success = false
  $scope.success_msg = ""

  $scope.logme = (function (){

   $http.post('/login/log/', {'username':$scope.username,'passw':$scope.raw_passw}).then(function(req) {

     $scope.success = req.data['success']
     if($scope.success){
       $scope.success_msg = "Successfully logged in."
     }else{
       $scope.error = "Your login is incorrect."
     }
      },
      function(err){
        //$log.log(err)

      });

    });

    $scope.create = (function (){

     $http.post('/login/create/', {'username':$scope.username,'passw':$scope.raw_passw}).then(function(req) {

       $scope.success = req.data['success']
       if($scope.success){
         $scope.success_msg = "Successfully created account please login."
       }else{
         $scope.error = "Your account could not be created."
       }
        },
        function(err){
          //$log.log(err)

        });

      });

}]);
