#pragma once

#include "ofMain.h"
#include "ofxOsc.h"
#include "ofxZmq.h"
#include "ScreenConsole.h"
#include "ofxThreadedImageLoader.h"

#define HOST "127.0.0.1"
#define PORT 54415

class ofApp : public ofBaseApp {

public:
	void setup();
	void update();
	void draw();
	ofxOscReceiver receiver;
	float oscMessage;
	float vol;
	ofxZmqSubscriber sub;
	ScreenConsole console;
	ofImage cameraImage;
	ofImage firstImage;
	ofImage secondImage;
	ofImage thirdImage;
	ofxThreadedImageLoader loader;
	vector<ofImage> images;
	int total;
	
	ofShader shader;
	ofFbo fbo;
	ofEasyCam cam;
};