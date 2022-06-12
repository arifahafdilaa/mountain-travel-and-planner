# Mountain Travel and Planner App (ML)
A travel-planner mobile application which specialize in mountain hiking. This project intended to fulfill Bangkit Academy 2022 program.

### Dataset 
There are three datasets used in this project : 
* Mountains, which is list of mountains available in Sumatra, Jawa, Bali and Nusa Tenggara. Some details information provided are included id, name, description, location, level of difficulty and whether it still active or not.
* Users, which is list of dummy users with detail information such as id, name, email, phone and address. 
* Ratings, whish is list of previous trips from all dummy user and how they rate it in scale of 1-5. Each users are assigned to  at least three to ten previous hiking trips. 

Since there are no suitable datasets available online, we decided to made our own datasets. For mountain dataset, the data were crawled manually from various online site. For users and ratings dataset, both were purely made through some process of randomization. 

### Recommendation System (Collaborative Filtering)
One of the features that this app provides is a list of mountain recommendations to help users plan their next hiking trip. To achieve this, we built a personalized recommendation system that will estimate each user's preferences using machine learning. There are several possible ways to do it, but for this project we decided to implement a recommendation system that based on users' previous rating score. Basically, our model will predict how a particular user will rate each available mountains. This results will works as a representation of whether they will enjoy hiking there or not. Then, the result is sorted out from the highest one and were given as recommendation.

### Deployment using Flask and Google Compute Engine
To deploy our model, we decided to use Flask API and run it using virtual machine on google compute engine. The Flask API will receives id user and return ten mountain ids based on the prediction result. As additional information, it wil also show the name of the mountains for all those ids that were called from Cloud Firestore using REST API. 

* Base URL : `http://34.101.162.201:5000/`
* Method : `POST`
* Request example : `http://34.101.162.201:5000/predict/1` 
* Result example :   

```javascript
    {
        "data":1,
        "name":["Gunung Lakaan","Gunung Welirang","Gunung Marapi","Gunung Baluran","Gunung Gambiran","Gunung Pangparang","Gunung Singgalang","Gunung Kumbang","Gunung Kembar I","Gunung Krakatau"],
        "prediction":[34,171,199,128,138,74,203,149,146,189]
    }
```

### Reference
* [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework))
* [Deploying an ML Model on Google Compute Engine](https://towardsdatascience.com/deploying-a-custom-ml-prediction-service-on-google-cloud-ae3be7e6d38f)
