var mainPanelApp = angular.module('mainPanelApp', []);
mainPanelApp.controller('mainPanelCtrl', ['$scope','$http','$log', function($scope,$http,$log) {
$scope.show_derivative = false
$scope.show_item_selection = false
$scope.show_edit_names = false
$scope.success_names = false
$scope.display_edit_names = (function () {
  $scope.show_item_selection = false
  $scope.show_derivative = false
  $scope.show_edit_names = true
});
$scope.display_derivative = (function () {
  $scope.show_derivative = true
  $scope.show_item_selection = false
  $scope.show_edit_names = false
});
$scope.display_item_selection = (function () {
  $scope.show_item_selection = true
  $scope.show_derivative = false
  $scope.show_edit_names = false
});
$scope.getDerivative = (function(){
  if($scope.function == ''){

  }else{
    $http.post('/derivative/derive/', {'function':$scope.function}).then(function(req) {

      $scope.derivative = req.data['derivative']

       },
       function(err){
         $log.log(err)

       });
     }
  });
$scope.getNames = (function (){
  $http.post('/main/editName/', {'name1':$scope.name1,'name2':$scope.name2,'name3':$scope.name3}).then(function(req) {

    $scope.success_names = req.data['success']

     },
     function(err){
       $log.log(err)

     });
});
}]);
