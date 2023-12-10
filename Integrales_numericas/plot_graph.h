#include <opencv2/opencv.hpp>
#include<vector>

using namespace std;

float find_max(vector<float>values){
   float max=values[0];
   for(float &pair:values){
      if(pair>max){
         max=pair;
      }
   }
   return max;
}

void plot_graph(vector<float>dots){
   if(dots.empty()){
      cerr<<"Error";
      return;
   }else{
      cout<<dots.size()<<'\n';
   }
   int vect_size=dots.size();
   float step=float(vect_size/400);
   float max=find_max(dots);
   cout<<"max "<<max<<'\n';
   float scale=200/max;


   cv::Mat *graphic=new cv::Mat(200,400,CV_8UC1,cv::Scalar(255));
   int pos=0;
   int aux_value;
   for (int i = 0; i < 400; i++){
      pos=i*step;
      cout<<scale*dots[pos]<<" sin escala: "<<dots[pos]<<" \n";
      for(int j=scale*dots[pos];j<200;j++){
         graphic->at<uchar>(j,i)=0;
      }
   }
   cv::imshow("Funcion",*graphic);
   cv::waitKey(0);
   delete(graphic);
   

}