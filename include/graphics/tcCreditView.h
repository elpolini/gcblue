/**
**  @file tcCreditView.h
*/
/*
**  Copyright (c) 2014, GCBLUE PROJECT
**  All rights reserved.
**
**  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
**
**  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
**
**  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the 
**     documentation and/or other materials provided with the distribution.
**
**  3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from 
**     this software without specific prior written permission.
**
**  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT 
**  NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE 
**  COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
**  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
**  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING 
**  IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/


#ifndef _CREDITVIEW_H_
#define _CREDITVIEW_H_

#if _MSC_VER > 1000
#pragma once
#endif

#include "wx/wx.h" 

#include "tc3DWindow2.h"
#include "tcSound.h"
#include "AError.h"
#include "tcString.h"

/**
* View window to display scrolling credits
*/
class tcCreditView : public tc3DWindow2
{
    struct tsCreditInfo
    {
        tcString mzCaption;
        float mfTrailSpace;
        int mnEffect; ///< 0 - standard text, 1 - bold, 2 - small
    };
public:
    void AddCredit(const tcString& s, float afTrailSpace, int effect);
    void Init();
    void Draw();
    void OnLButtonDown(wxMouseEvent& event);
    void OnSize(wxSizeEvent& event);
    void Rewind();

    tcCreditView(wxWindow* parent, 
        const wxPoint& pos, const wxSize& size, 
        const wxString& name = "CreditView");

    tcCreditView(tc3DWindow2* parent, 
        const wxPoint& pos, const wxSize& size, 
        const wxString& name);

    virtual ~tcCreditView();
private:
    enum {MAX_CREDITS = 96};
    //Gdiplus::SolidBrush *mpBrush;
    //Gdiplus::Font *mpFont;
    //Gdiplus::Font *mpFontLarge;
    //Gdiplus::Font *mpFontSmall;
    //Gdiplus::Pen *mpPen;
    unsigned int mnStartTime; // 30 Hz counter to mark start of sequence

    tcString crawlstring;
    tsCreditInfo maCredit[MAX_CREDITS];
    unsigned mnCredits;
    bool mbDrawRewind; // flag to reset Draw() method 
};

#endif