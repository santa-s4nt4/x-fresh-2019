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
	float osc1;
	float osc2;
	float osc3;
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

	void audioIn(ofSoundBuffer & input);

	vector <float> left;
	vector <float> right;
	vector <float> volHistory;

	int bufferCounter;
	int drawCounter;

	float smoothedVol;
	float scaledVol;

	ofSoundStream soundStream;
};