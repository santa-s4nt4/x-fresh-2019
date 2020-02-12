#pragma once

#include "ofMain.h"
#include "ofxOsc.h"
#include "ofxZmq.h"
#include "ScreenConsole.h"
#include "ofxThreadedImageLoader.h"
#include "ofxSpout.h"

#define HOST "127.0.0.1"
#define PORT 54415

class ofApp : public ofBaseApp {

public:
	void setup();
	void update();
	void draw();
	ofxOscReceiver receiver;
	float oscMessage;
	ofxZmqSubscriber sub;
	ScreenConsole console;
	ofImage cameraImage;
	ofImage firstImage;
	ofImage secondImage;
	ofImage thirdImage;
	ofxThreadedImageLoader loader;
	vector<ofImage> images;
	int total;
	ofxSpout::Sender sender;

	ofShader shader;
	ofFbo fbo;
	ofEasyCam cam;
};