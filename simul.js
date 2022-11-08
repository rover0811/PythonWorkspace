
  function car_info(){
    this.regi_num="36조 1602";
    this.car_type="YF 소나타";
    this.is_resident="1";
    this.visit_purpose="방문";
  }
  
  function time_info(){
    this.entrace_time="2022-08-02-13-20";
    this.departure_time="2022-08-02-19:34";
  }
  
  function ta_history(){
    this.num_of_ta="0";
    this.is_facility_damage="0";
    this.is_people_damage="0";
  }
  
  class Car{   //클래스로 만들어보기
    constructor(){
      this.car_info=new car_info();
      this.time_info=new time_info();
      this.ta_history=new ta_history();
    }
  }
  
  function rand(min, max) {//Max값 포함 랜덤 함수 -> 가중치 랜덤함수도 만들어야함
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  
  let timeline=[50,20,10,5,5,10,50,100,300,100,50,200,100,30,40,30,60,70,80,90,100,200,300,400]
  var sum = timeline.reduce(function(a, b){ return a + b; }, 0);
  // console.log(sum);
  
  
  
  
  let Sedan_type_array=['제네시스','그랜저','소나타','아반떼','펠리세이드','투싼','싼타페','모닝','쏘렌토','카니발','K5']
  let hangeulSedan=['가','나','다','라','마','거','너','더','러','머','버','서','어','저','고','노','도','로','모','보','소','오','조']
  let Binary=["Y","N"]
  
  
  class Sedan extends Car{
    constructor(timeData){
      super()
      this.car_info.regi_num=rand(1,69)+hangeulSedan[rand(0,hangeulSedan.length-1)]+rand(1000,9999)
      this.car_info.car_type=Sedan_type_array[rand(0,Sedan_type_array.length-1)]
      this.car_info.is_resident=Binary[rand(0,1)]
      this.time_info.entrace_time=new Date(timeData)
    }
  }
  let testList=new Array();
  let start=new Date('2022-08-01 00:01:00');
  let temp=new Date('2022-08-01 00:01:00');
  
  
  for (let i=0; i<timeline.length;i++){ //차량 대수
    let interval=60*60/timeline[i] ;
    for(let k=0; k<timeline[i];k++){
      testList.push(new Sedan(start));
      start.setSeconds(start.getSeconds()+interval)
    }
    start.setHours(temp.getHours(temp.getHours()+1));\


    
  };
  let jsonData=JSON.stringify(testList);

  let fs = require('fs');
fs.writeFile("test.json", jsonData, function(err) {
    if (err) {
        console.log(err);
    }
});