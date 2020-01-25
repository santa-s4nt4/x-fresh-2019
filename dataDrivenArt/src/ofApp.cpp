#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
	receiver.setup(PORT);

	fbo.allocate(ofGetWidth(), ofGetHeight());

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

		oscMessage = m.getArgAsInt32(0);
		console("address") << oscMessage << " " << m.getNumArgs();

		cameraImage.load("export/export.png");

		if (m.getAddress() == "/first") {
			std::string front = "images/";
			std::string back = ".jpg";
			std::string path = front + std::to_string(oscMessage) + back;
			console(path);
			firstImage.load(path);
		}

		if (m.getAddress() == "/second") {
			std::string front = "images/";
			std::string back = ".jpg";
			std::string path = front + std::to_string(oscMessage) + back;
			console(path);
			secondImage.load(path);
		}

		if (m.getAddress() == "/third") {
			std::string front = "images/";
			std::string back = ".jpg";
			std::string path = front + std::to_string(oscMessage) + back;
			console(path);
			thirdImage.load(path);
		}
	}
}

//--------------------------------------------------------------
void ofApp::draw(){
	fbo.begin();

	cameraImage.draw(0, ofGetHeight() / 2, ofGetWidth() / 2, ofGetHeight() / 2);
	firstImage.draw(0, 0, ofGetWidth() / 2, ofGetHeight() / 2);
	secondImage.draw(ofGetWidth() / 2, 0, ofGetWidth() / 2, ofGetHeight() / 2);
	thirdImage.draw(ofGetWidth() / 2, ofGetHeight() / 2, ofGetWidth() / 2, ofGetHeight() / 2);
	
	fbo.end();

	console.print(40, 40);
}