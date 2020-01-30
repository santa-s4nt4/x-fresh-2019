#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
	ofEnableDepthTest();

	shader.load("shader/shader.vert", "shader/shader.frag");

	fbo.allocate(ofGetWidth(), ofGetHeight());

	receiver.setup(PORT);

	sub.connect("tcp://127.0.0.1:54414");

	ofDirectory dir(ofToDataPath("./images/"));

	total = dir.listDir();
	
	images.resize(total);

	for (int i = 0; i < total; i++) {
		loader.loadFromDisk(images[i], dir.getName(i));
		images[i].resize(640, 480);
	}
	cout << total << " images loaded" << endl;
}

//--------------------------------------------------------------
void ofApp::update(){
	while (receiver.hasWaitingMessages()) {
		ofxOscMessage m;

		receiver.getNextMessage(m);

		oscMessage = m.getArgAsFloat(0);
		console("address") << oscMessage << " " << m.getNumArgs();

		if (m.getAddress() == "/vol") {
			std::string oscVol = std::to_string(oscMessage);
			console(oscVol);
		}
	}
	
	while (sub.hasWaitingMessage()) {
		cameraImage.load("cam/export.png");

		std::string msg;
		sub.getNextMessage(msg);
		std::string img1 = msg.substr(0, 4);
		std::string img2 = msg.substr(5, 4);
		std::string img3 = msg.substr(10, 4);

		console(img1);
		console(img2);
		console(img3);

		std::string path1 = "images/" + img1 + ".jpg";
		std::string path2 = "images/" + img2 + ".jpg";
		std::string path3 = "images/" + img3 + ".jpg";
		firstImage.load(path1);
		secondImage.load(path2);
		thirdImage.load(path3);
	}
}

//--------------------------------------------------------------
void ofApp::draw(){
	console.print(40, 40);

	fbo.begin();
	ofClear(0, 0, 0, 0);
	ofPushMatrix();
	ofTranslate(ofGetWidth() / 2, ofGetHeight() / 2);

	cam.begin();

	cam.end();

	ofPopMatrix();

	cameraImage.draw(0, ofGetHeight() / 2, ofGetWidth() / 2, ofGetHeight() / 2);
	firstImage.draw(0, 0, ofGetWidth() / 2, ofGetHeight() / 2);
	secondImage.draw(ofGetWidth() / 2, 0, ofGetWidth() / 2, ofGetHeight() / 2);
	thirdImage.draw(ofGetWidth() / 2, ofGetHeight() / 2, ofGetWidth() / 2, ofGetHeight() / 2);

	fbo.end();

	// PostEffect
	shader.begin();
	shader.setUniformTexture("texture", fbo, 0);
	shader.setUniform2f("resolution", ofGetWidth(), ofGetHeight());
	shader.setUniform1f("vol", oscMessage);
	shader.setUniform1f("time", ofGetElapsedTimef());

	ofDrawRectangle(0, 0, ofGetWidth(), ofGetHeight());
	shader.end();
}
