/** 
**  @file tcBoundingBoxVisitor.cpp 
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
/*
**  Based on code by Farshid Lashkari posted to the osg-users list on April 18, 2006
*/


#include "stdwx.h" // precompiled header file

#ifndef WX_PRECOMP
#include "wx/wx.h" 
#endif // WX_PRECOMP

#include "tcBoundingBoxVisitor.h"

#include <osg/BoundingBox>
#include <osg/Geode>
#include <osg/Transform>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif



void tcBoundingBoxVisitor::apply(osg::Node &node)
{
	traverse(node);
}

void tcBoundingBoxVisitor::apply(osg::Geode &geode)
{
	for(unsigned int i = 0; i < geode.getNumDrawables(); i++) 
	{
		osg::BoundingBox bb = geode.getDrawable(i)->getBound();
		m_bb.expandBy(bb.corner(0)*m_curMatrix);
		m_bb.expandBy(bb.corner(1)*m_curMatrix);
		m_bb.expandBy(bb.corner(2)*m_curMatrix);
		m_bb.expandBy(bb.corner(3)*m_curMatrix);
		m_bb.expandBy(bb.corner(4)*m_curMatrix);
		m_bb.expandBy(bb.corner(5)*m_curMatrix);
		m_bb.expandBy(bb.corner(6)*m_curMatrix);
		m_bb.expandBy(bb.corner(7)*m_curMatrix);
	}
	traverse(geode);
}

void tcBoundingBoxVisitor::apply(osg::Transform& node)
{
	osg::Matrix matrix;
	node.computeLocalToWorldMatrix(matrix, this);

	osg::Matrix prevMatrix = m_curMatrix;
	m_curMatrix.preMult(matrix);

	traverse(node);

	m_curMatrix = prevMatrix;
}

osg::BoundingBox tcBoundingBoxVisitor::getBound() const
{
	return m_bb;
}



tcBoundingBoxVisitor::tcBoundingBoxVisitor(const osg::Matrix &mat) : osg::NodeVisitor(TRAVERSE_ALL_CHILDREN)
{
	m_curMatrix = mat;
}


