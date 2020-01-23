#pragma once

#include "ofMain.h"
#include "ofxOsc.h"
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
	int oscMessage;
	ScreenConsole console;
	ofImage cameraImage;
	ofImage artImage;
	ofxThreadedImageLoader loader;
	vector<ofImage> images;
	int total;
};